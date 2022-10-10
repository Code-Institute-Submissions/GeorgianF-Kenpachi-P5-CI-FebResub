from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/<product_id>', views.add_to_bag, name='add_to_bag'),
    path('item_update/', views.item_update, name="item_update"),
]
