from django.urls import path
from . import views

urlpatterns = [
    path('', views.novel_list, name='novel_list'),
]
