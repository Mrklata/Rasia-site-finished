from django.urls import path
from look import views

urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('closet/', views.closet, name='closet'),
    path('beds/', views.beds, name='beds'),
    path('movies/', views.movies, name='movies'),
    path('other/', views.other, name='other'),
    path('from_back/', views.from_back, name='from_back'),
]