from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserSetting, CalorieEntry
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'
        read_only_fields = ('user',)


class CalorieEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieEntry
        fields = ['text', 'calories']

    def create(self, validated_data):
        # Parse date and time strings into date and time objects
        validated_data['date'] = datetime.date.today()
        validated_data['time'] = datetime.datetime.now().time()


        return CalorieEntry.objects.create(**validated_data)


class CalorieEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieEntry
        fields = '__all__'