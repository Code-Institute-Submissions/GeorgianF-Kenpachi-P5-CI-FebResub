from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('process_order/', views.process_order, name='process_order'),
    path('config/', views.stripe_config),
]
