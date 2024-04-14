from django.urls import path
from . import views

urlpatterns = [
    path('profiles', views.profiles, name='profiles'),
    path('', views.home, name='home'),
    path('someonesprofile/<int:pk>', views.someonesprofile, name='someonesprofile'),
    
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    
    path('register/', views.register, name='register'),
    
    path('update_user/', views.update_user, name="update_user")
]

