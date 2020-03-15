from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_product', views.add_product, name='add_product'),
    path('update_product/<str:pk>/', views.update_product, name='update_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product')
]