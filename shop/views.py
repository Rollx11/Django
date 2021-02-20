from django.shortcuts import render
from .models import Drink
from .forms import Loginsform



def index(request):
    drinks = Drink.objects.all()
    return render(request, 'shop/index.html', {'title': 'Главная страница сайта', 'drinks': drinks})


def about(request):
    return render(request, 'shop/about.html',)


def login(request):
    form = Loginsform()

    if request.method == 'POST':
        form = Loginsform(request.POST)
        if form.is_valid():
            form.save()

    context = { 'form': form }
    return render(request, 'shop/login.html', context )