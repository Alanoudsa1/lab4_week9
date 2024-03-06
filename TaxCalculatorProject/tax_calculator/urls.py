from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('<int:num>/', views.calculate_total_price, name='calculate_total_price'),
    path('taxrate/', views.tax_rate_view, name='tax_rate_view'),
] 