from django.db import models


class HeritageSite(models.Model):
    # Core identity
    site_id = models.SlugField(unique=True, max_length=100)  # e.g. "bangalore-palace"
    place_id = models.CharField(max_length=200, blank=True)  # Google Places ID
    type_tag = models.CharField(max_length=50, blank=True, help_text="e.g. PALACE, FORT, PARK")

    # Location
    lat_lng = models.CharField(max_length=50)               # e.g. "12.9988,77.5921"
    address = models.TextField(blank=True)

    # Hero section
    hero_image = models.URLField(max_length=1000)
    title_line1 = models.CharField(max_length=100)
    title_line2 = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300, blank=True)

    # Hero overrides (optional Tailwind color classes)
    hero_title_color = models.CharField(max_length=100, blank=True)
    hero_subtitle_color = models.CharField(max_length=100, blank=True)
    hero_title_weight = models.CharField(max_length=100, blank=True)
    metric_text_color = models.CharField(max_length=100, blank=True)

    # History section
    history_title = models.TextField()
    history_paragraph1 = models.TextField()
    history_paragraph2 = models.TextField(blank=True)
    history_paragraph3 = models.TextField(blank=True)
    history_image1 = models.URLField(max_length=1000, blank=True)
    history_image2 = models.URLField(max_length=1000, blank=True)

    # Video section
    video_title = models.CharField(max_length=200, blank=True)
    video_subtitle = models.CharField(max_length=200, blank=True)
    youtube_id = models.CharField(max_length=50, blank=True)

    # Gallery
    gallery_title = models.CharField(max_length=200, blank=True)
    gallery_subtitle = models.CharField(max_length=200, blank=True)
    gallery_images = models.JSONField(default=list)          # list of image URLs

    # Metrics (list of {label, value, span?})
    metrics = models.JSONField(default=list)

    # Theme colours (Tailwind class strings)
    theme_text_root = models.CharField(max_length=100, blank=True)
    theme_border_light = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_line1']

    def __str__(self):
        return f"{self.title_line1} {self.title_line2}"
