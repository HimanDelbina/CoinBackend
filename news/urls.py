from django.urls import path
from news import views

urlpatterns = [
    path('news_list', views.get_news_list),
]
