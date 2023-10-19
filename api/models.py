from django.db import models
from django.contrib.auth.models import User

class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expected_calories_per_day = models.PositiveIntegerField()

class CalorieEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField()
    calories = models.PositiveIntegerField(null=True)
    is_under_expected_calories = models.BooleanField(default=False)
