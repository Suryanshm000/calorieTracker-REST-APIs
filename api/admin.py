from django.contrib import admin
from .models import UserSetting, CalorieEntry

# Register your models here.
admin.site.register(UserSetting)
admin.site.register(CalorieEntry)
