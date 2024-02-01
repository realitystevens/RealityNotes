from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('a/', views.article, name='article'),
    path('a/<str:url_hash>', views.article_detail, name='article_detail'),
]