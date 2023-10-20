from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    path('user/create', views.CreateUserView.as_view(), name='user-create'),
    path('user/login', obtain_auth_token, name='user-login'),
    path('user/set_calorie', views.UserSettingCreate.as_view(), name='usersetting'),
    path('user/entry', views.CalorieEntryCreateView.as_view(), name='entry-create'), 
    path('user/view_entry', views.CalorieEntryListView.as_view(), name='entry-list'), 
    path('user/entry/<int:pk>', views.CalorieEntryRetrieveDestroyView.as_view(), name='entry-detail'),
    path('user/entry_update/<int:pk>', views.CalorieEntryUpdateView.as_view(), name='entry-update'),
    path('user/set_usermanager/<int:pk>', views.SetUserManager.as_view(), name='usermanager-update'),
    path('user/<int:pk>', views.UserManagerRetrieveDestroyView.as_view(), name='user-detail-delete'),
    path('users', views.UserManagerListView.as_view(), name='user-list'),
    path('user/update/<int:pk>', views.UserManagerUpdateView.as_view(), name='user-update'),
]