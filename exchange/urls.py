from django.urls import path
from exchange import views

urlpatterns = [
    path('exchange_list', views.get_exchange_list),
]
