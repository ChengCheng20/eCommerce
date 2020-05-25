from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('glasses.html', views.glasses, name='glasses'),
    path('shop.html', views.shop, name='shop'),
]