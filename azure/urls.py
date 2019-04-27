from django.urls import path
from . import views

urlpatterns = [
    path('', views.novel_list, name='novel_list'),
    path('post/<int:pk>/', views.novel_detail, name='novel_detail'),
]
