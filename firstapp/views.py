from django.shortcuts import render
from django.http import HttpResponse
from teacher.models import *


def index(request):
    add = Teacher.objects.all()
    context = {
        "add": add
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, "about.html")


def courses(request):
    return render(request, "courses.html")


def team(request):
    return render(request, "team.html")


def testimonial(request):
    return render(request, "testimonial.html")


def contact(request):
    return render(request, "contact.html")


def index1(request):
    return render(request, "index1.html")


def koreys_tili(request):
    return render(request, "koreys_tili.html")


def ingliz_tili(request):
    return render(request, "ingliz_tili.html")


def rus_tili(request):
    return render(request, "rus_tili.html")
