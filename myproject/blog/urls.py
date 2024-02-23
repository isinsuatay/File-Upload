from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_with_message/', views.index_with_message, name='index_with_message'),
]
