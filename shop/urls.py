from django.urls import path
import shop.views as v

urlpatterns = [
    path('', v.index, name="home"),
    path('about', v.about, name='about'),
    path('login', v.login, name='login'),
]