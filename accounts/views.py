from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer

class SignupView(APIView):
    def post(self, request):
        data = request.data.copy()
        if not data.get('username') and data.get('email'):
            data['username'] = data.get('email').split('@')[0]

        if data.get('password') != data.get('confirm_password'):
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data.get('email', ''),
                password=serializer.validated_data['password']
            )
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


# import secrets
# from django.contrib.auth.hashers import make_password, check_password
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .db import users_collection, tokens_collection

# class SignupView(APIView):
#     def post(self, request):
#         data     = request.data
#         username = data.get("username")
#         email    = data.get("email", "")
#         password = data.get("password")
#         confirm  = data.get("confirm_password")

#         if not username and email:
#             username = email.split("@")[0]

#         if password != confirm:
#             return Response({"error": "Passwords do not match"}, status=400)

#         if users_collection.find_one({"username": username}):
#             return Response({"error": "Username already exists"}, status=400)

#         user_id = str(users_collection.insert_one({
#             "username": username,
#             "email":    email,
#             "password": make_password(password),
#         }).inserted_id)

#         token = secrets.token_hex(20)
#         tokens_collection.insert_one({"user_id": user_id, "token": token})

#         return Response({"token": token, "user_id": user_id}, status=201)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         user = users_collection.find_one({"username": username})
#         if not user or not check_password(password, user["password"]):
#             return Response({"error": "Invalid Credentials"}, status=400)

#         user_id  = str(user["_id"])
#         existing = tokens_collection.find_one({"user_id": user_id})
#         token    = existing["token"] if existing else secrets.token_hex(20)

#         if not existing:
#             tokens_collection.insert_one({"user_id": user_id, "token": token})

#         return Response({"token": token, "user_id": user_id}, status=200)
