from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_page"),
    path("register/", views.register, name="register_page"),
    path("login/", views.login, name="login_page"),
    path('home/',views.home,name='home_url'),
    path('profile/',views.profile,name='profile_url'),
]
