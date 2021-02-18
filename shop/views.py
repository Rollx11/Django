
from django.shortcuts import render
from .models import Drink


def index(request):
    drinks = Drink.objects.all()
    return render(request, 'shop/index.html', {'title': 'Главная страница сайта', 'drinks': drinks})


def about(request):
    return render(request, 'shop/about.html',)


def login(request):
    return render(request, 'shop/login.html',)