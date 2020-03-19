from django.shortcuts import render
from look.models import Image, Movie


def main_site(request):
    return render(request, 'look/main_site.html')


def bathroom(request):
    file = Image.objects.filter(section='bathroom')
    return render(request, 'look/bathroom.html', {'file': file})


def kitchen(request):
    file = Image.objects.filter(section='kitchen')
    return render(request, 'look/kitchen.html', {'file': file})


def closet(request):
    file = Image.objects.filter(section='closet')
    return render(request, "look/closet.html", {'file': file})


def beds(request):
    file = Image.objects.filter(section='beds')
    return render(request, 'look/beds.html', {'file': file})


def other(request):
    file = Image.objects.filter(section='other')
    return render(request, 'look/other.html', {'file': file})


def movies(request):
    file = Movie.objects.all()
    return render(request, 'look/movies.html', {'file': file})


def from_back(request):
    file = Image.objects.filter(section='back')
    return render(request, 'look/from_back.html', {'file': file})
# Create your views here.
