from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('category/<id>/', views.category, name='category'),
    path('item/<id>/', views.item_detail, name='item_detail'),
    path('item/<item_id>/add_review', views.add_review, name='add_review'),
    path('item/<item_id>/to_basket', views.to_basket, name='to_basket'),
    path('basket/', views.basket_view, name='basket_view'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_order', views.create_order, name='create_order'),
    path('delete_order', views.delete_order, name='delete_order')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)