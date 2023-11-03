from django.contrib import admin
from django.urls import path

from frontent import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/',views.productpage,name="productpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('filterdpage/',views.filterdpage,name="filterdpage"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('login_user/',views.login_user,name="login_user"),
    path('login_page/',views.login_page,name="login_page"),
    ]