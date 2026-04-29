from rest_framework import serializers
from .models import HeritageSite, Review

class ReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='user.username', read_only=True)
    relative_time_description = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ['id', 'author_name', 'text', 'rating', 'relative_time_description', 'created_at']

    def get_relative_time_description(self, obj):
        from django.utils import timezone
        now = timezone.now()
        diff = now - obj.created_at
        if diff.days == 0:
            return "Today"
        elif diff.days == 1:
            return "1 day ago"
        elif diff.days < 30:
            return f"{diff.days} days ago"
        elif diff.days < 365:
            return f"{diff.days // 30} months ago"
        return f"{diff.days // 365} years ago"


class HeritageSiteSerializer(serializers.ModelSerializer):
    """
    Returns JSON shaped to match the existing frontend heritageSites.js structure
    so the React code needs minimal changes.
    """

    # Computed fields to reconstruct nested objects the frontend expects
    id = serializers.CharField(source='site_id')
    typeTag = serializers.CharField(source='type_tag')
    placeId = serializers.CharField(source='place_id')
    latLng = serializers.CharField(source='lat_lng')
    heroImage = serializers.URLField(source='hero_image')
    title = serializers.SerializerMethodField()
    subtitle = serializers.CharField()
    heroTitleColor = serializers.CharField(source='hero_title_color')
    heroSubtitleColor = serializers.CharField(source='hero_subtitle_color')
    heroTitleWeight = serializers.CharField(source='hero_title_weight')
    metricTextColor = serializers.CharField(source='metric_text_color')
    history = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    galleryTitle = serializers.CharField(source='gallery_title')
    gallerySubtitle = serializers.CharField(source='gallery_subtitle')
    gallery = serializers.JSONField(source='gallery_images')
    metrics = serializers.JSONField()
    address = serializers.CharField()
    theme = serializers.SerializerMethodField()
    local_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = HeritageSite
        fields = [
            'id', 'typeTag', 'placeId', 'latLng', 'heroImage',
            'title', 'subtitle',
            'heroTitleColor', 'heroSubtitleColor', 'heroTitleWeight', 'metricTextColor',
            'history', 'video',
            'galleryTitle', 'gallerySubtitle', 'gallery',
            'metrics', 'address', 'theme', 'local_reviews',
        ]

    def get_title(self, obj):
        return [obj.title_line1, obj.title_line2]

    def get_history(self, obj):
        paragraphs = [p for p in [
            obj.history_paragraph1,
            obj.history_paragraph2,
            obj.history_paragraph3,
        ] if p]
        return {
            'title': obj.history_title,
            'paragraphs': paragraphs,
            'image1': obj.history_image1,
            'image2': obj.history_image2,
        }

    def get_video(self, obj):
        return {
            'title': obj.video_title,
            'subtitle': obj.video_subtitle,
            'youtubeId': obj.youtube_id,
        }

    def get_theme(self, obj):
        return {
            'textRoot': obj.theme_text_root,
            'borderLight': obj.theme_border_light,
        }
