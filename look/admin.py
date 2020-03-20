from django.contrib import admin
from .models import Image, Movie, BackgroundImage

admin.site.register(Image)
admin.site.register(Movie)
admin.site.register(BackgroundImage)