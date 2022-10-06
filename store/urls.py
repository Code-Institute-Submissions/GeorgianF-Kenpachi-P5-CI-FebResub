from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('item_update/', views.item_update, name="item_update"),
]
