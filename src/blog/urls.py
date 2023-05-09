from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='explore'),
    path('post/<pk>', views.SingleBlog, name='post')
]