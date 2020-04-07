from django.shortcuts import render
from look.models import Image, Movie


def main_site(request):
    return render(request, 'look/main_2.html')


def bathroom(request):
    file = Image.objects.filter(section='bathroom')
    return render(request, 'look/bathroom_2.html', {'file': file})


def kitchen(request):
    file = Image.objects.filter(section='kitchen')
    return render(request, 'look/kitchen2.html', {'file': file})


def closet(request):
    file = Image.objects.filter(section='closet')
    return render(request, "look/closet2.html", {'file': file})


def beds(request):
    file = Image.objects.filter(section='beds')
    return render(request, 'look/beds2.html', {'file': file})


def other(request):
    file = Image.objects.filter(section='other')
    return render(request, 'look/others2.html', {'file': file})


def movies(request):
    file = Movie.objects.all()
    return render(request, 'look/movies2.html', {'file': file})


def from_back(request):
    file = Image.objects.filter(section='back')
    return render(request, 'look/from_back2.html', {'file': file})


def main_try(request):
    return render(request, 'look/main_2.html')
# Create your views here.
