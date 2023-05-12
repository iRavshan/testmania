from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('', views.Home, name='blog'),
    path('post/<pk>', views.SingleBlog, name='post')
]