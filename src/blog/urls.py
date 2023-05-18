from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='news'),
    path('<uuid:id>', views.SingleBlog, name='post')
]