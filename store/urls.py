from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path(
        'contact/view_message/<message_id>',
        views.view_message,
        name='view_message'
        ),
    path(
        'contact/delete/<int:message_id>',
        views.delete_message,
        name='delete_message'
        ),
    path(
        'category/<slug:category_slug>/',
        views.store,
        name='products_by_category'
        ),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),
    path('item_update/', views.item_update, name="item_update"),
    path(
        '<int:product_id>/item_update/',
        views.product_details_add,
        name='product_details_add'
        ),
    path('profile/', views.profile, name="profile"),
    path('profile/<str:transaction_id>', views.view_order, name="view_order"),
    path('add_product', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/', views.delete_product, name='delete_product'
        ),
    path(
        'reset_password',
        auth_views.PasswordResetView.as_view(
            template_name="./account/password_reset.html"
            ),
        name='reset_password'),
    path(
        'reset_password_done',
        auth_views.PasswordResetDoneView.as_view(
            template_name="./account/password_reset_done.html"
        ),
        name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="./account/password_reset_from_key.html"
        ),
        name='password_reset_confirm'),
    path(
        'reset_password_complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="./account/password_reset_from_key_done.html"
        ),
        name='password_reset_complete'),
]
