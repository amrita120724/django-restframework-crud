from django.urls import path
from .views import get_users, create_user, single_user

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:pk>', single_user, name='single_user')
]
