from django.urls import path
from . import views

urlpatterns = [
    path('', views.novel_list, name='novel_list'),
    path('novel/<int:pk>/', views.novel_detail, name='novel_detail'),
    path('curate/', views.curate_novel_list, name='curate_novel_list'),
]
