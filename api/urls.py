from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    path('user/create', views.CreateUserView.as_view(), name='user-create'),
    path('user/login', obtain_auth_token, name='user-login'),
]