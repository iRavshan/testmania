from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='tests'),
    path('<pk>', views.GetTest, name='test'),
    path('checkanswers/<pk>', views.CheckAnswers, name='checkanswers'),
    path('get-file/<pk>', views.SendFile, name='getfile')
]