from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='news'),
    path('<str:title>', views.SingleBlog, name='post')
]