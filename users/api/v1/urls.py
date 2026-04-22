from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('v1/register/', UserRegisterView.as_view(), name='register'),
]