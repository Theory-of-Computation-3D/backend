from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('select', views.select),
    path('download', views.download)
]