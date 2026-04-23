from django.contrib import admin
from .models import HeritageSite


@admin.register(HeritageSite)
class HeritageSiteAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'title_line1', 'title_line2', 'address', 'updated_at')
    search_fields = ('site_id', 'title_line1', 'title_line2', 'address')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identity', {
            'fields': ('site_id', 'type_tag', 'place_id', 'lat_lng', 'address')
        }),
        ('Hero Section', {
            'fields': (
                'hero_image', 'title_line1', 'title_line2', 'subtitle',
                'hero_title_color', 'hero_subtitle_color', 'hero_title_weight', 'metric_text_color'
            )
        }),
        ('Metrics', {
            'fields': ('metrics',)
        }),
        ('History Section', {
            'fields': (
                'history_title',
                'history_paragraph1', 'history_paragraph2', 'history_paragraph3',
                'history_image1', 'history_image2'
            )
        }),
        ('Video Section', {
            'fields': ('video_title', 'video_subtitle', 'youtube_id')
        }),
        ('Gallery', {
            'fields': ('gallery_title', 'gallery_subtitle', 'gallery_images')
        }),
        ('Theme', {
            'fields': ('theme_text_root', 'theme_border_light')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
