from django.db import models
from embed_video.fields import EmbedVideoField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


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

    description = models.TextField(max_length=3000, help_text="Max 15 linijek")
    image = models.ImageField(upload_to='media')
    section = models.CharField(max_length=100, choices=SECTION)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(height=300)], format='JPEG',
                                     options={'quality': 70})


class Movie(models.Model):
    movie = EmbedVideoField()
    description = models.TextField(max_length=3000, help_text="Max 15 linijek")

# Create your models here.
