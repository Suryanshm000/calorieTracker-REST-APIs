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

    def validate_expected_calories_per_day(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Calories cannot be negative.")
        return value


class CalorieEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieEntry
        fields = ['text', 'calories']

    def validate_calories(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Calories cannot be negative.")
        return value

    def create(self, validated_data):
        # Parse date and time strings into date and time objects
        validated_data['date'] = datetime.date.today()
        validated_data['time'] = datetime.datetime.now().time()


        return CalorieEntry.objects.create(**validated_data)


class CalorieEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieEntry
        fields = '__all__'


class SetUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_staff']


class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'