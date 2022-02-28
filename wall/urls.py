from django.urls import path
from wall import views

urlpatterns = [
    path('get_wall', views.get_wall),
]
