from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('story/', views.story, name='story'),
    path('test/', views.test_404, name='test'),
]
