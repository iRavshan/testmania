from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('settings/', views.Settings, name='settings'),
    path('<str:username>', views.Profile, name='profile')
]