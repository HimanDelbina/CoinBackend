from django.urls import path
from user import views

urlpatterns = [
    path('register', views.create_user),
    path('login', views.login),
    path('check_token', views.check_token),
    # path('forget_password', views.forget_password),
    # path('change_password', views.change_password),
    # path('access_levels', views.access_levels),
]
