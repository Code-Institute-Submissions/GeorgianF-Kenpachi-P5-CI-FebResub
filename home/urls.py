from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('story/', views.story, name='story'),
    path('contact/', views.contact, name='contact'),
]
