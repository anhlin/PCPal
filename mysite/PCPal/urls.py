from django.urls import path
from . import views

urlpatterns = [
    path('', views.cpu_index, name = 'cpu_index'),
  #  path('', views.gpu_index, name = 'gpu_index'),
]



