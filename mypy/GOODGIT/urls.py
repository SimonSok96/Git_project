from django.urls import path
from . import views

urlpatterns = [
    path('profiles', views.profiles, name='profiles'),
    path('', views.home, name='home'),
    path('someonesprofile/<int:pk>', views.someonesprofile, name='someonesprofile'),
]

