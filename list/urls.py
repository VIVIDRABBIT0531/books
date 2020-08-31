from django.urls import path
from . import views


app_name = 'list'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/detail/', views.detail, name='detail'),
]