from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from .models import HeritageSite
from .serializers import HeritageSiteSerializer


class HeritageSiteListView(APIView):
    """
    GET /api/sites/
    Returns all heritage sites as a list.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        sites = HeritageSite.objects.all()
        serializer = HeritageSiteSerializer(sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class HeritageSiteDetailView(APIView):
    """
    GET /api/sites/<site_id>/
    Returns a single heritage site by its slug id (e.g. 'bangalore-palace').
    """
    permission_classes = [AllowAny]

    def get(self, request, site_id):
        site = get_object_or_404(HeritageSite, site_id=site_id)
        serializer = HeritageSiteSerializer(site)
        return Response(serializer.data, status=status.HTTP_200_OK)
