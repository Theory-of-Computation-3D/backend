from django.urls import path
from . import views
from .views import download, downloadapi


urlpatterns = [
    path('', views.api_home),
    path('select', views.select),
    path('download.csv', views.download)
]