from django.db import models
from embed_video.fields import EmbedVideoField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from meta.models import ModelMeta


class Contact(models.Model):
    number = models.CharField(max_length=12, default=+48513294634)
    adress = models.CharField(max_length=100)


class Image(models.Model):
    SECTION = (
        ("bathroom", "łazienka"),
        ("kitchen", "kuchnia"),
        ("closet", "szafy"),
        ("beds", "łóżka"),
        ("other", "inne"),
        ("back", "zaplecze"),
    )

    description = models.TextField(max_length=3000, help_text="Max 15 linijek", null=True, blank=True)
    image = models.ImageField(upload_to='media')
    section = models.CharField(max_length=100, choices=SECTION)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(height=300)], format='JPEG',
                                     options={'quality': 70})

    def __str__(self):
        return self.description


class Movie(models.Model):
    movie = EmbedVideoField()
    description = models.TextField(max_length=3000, help_text="Max 15 linijek")


class Seo(ModelMeta, models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='meta')

    _metadata = {
        'title': 'name',
        'description': 'description',
        'image': 'get_meta_image',
    }

    def get_meta_image(self):
        if self.image:
            return self.image.url
