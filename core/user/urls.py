from django.urls import path
from .views.users.views import *

urlpatterns = [
    path('change/password/', UserChangePasswordView.as_view(), name='user_change_password'),
    path('change/profile/', UserUpdateProfileView.as_view(), name='user_profile'),
    path('change/profile/<int:pk>/', ChangeProfileView.as_view(), name='user_change_profile'),
]
