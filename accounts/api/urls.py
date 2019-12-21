from django.urls import path
from accounts.api import views



app_name = 'user'

urlpatterns = [
    path('register/',views.CreateUser.as_view(),name='register'),
]