from django.urls import path
from . import views

urlpatterns = [
    path('', views.novel_list, name='novel_list'),
    path('novel/<int:pk>/', views.novel_detail, name='novel_detail'),
    path('curate/', views.curate_novel_list, name='curate_novel_list'),
    path('curate/novel/<int:pk>/', views.curate_novel_detail, name='curate_novel_detail'),
    path('curate/novel/<int:pk>/edit/', views.curate_novel_edit, name='curate_novel_edit'),
]
