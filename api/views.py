from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import CalorieEntry
from .serializers import UserSerializer, UserSettingSerializer, CalorieEntrySerializer, CalorieEntryListSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserManager, IsAdmin
import datetime
from django.db.models import Sum
import requests, json


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        Token.objects.create(user=user)

## Expected calories entry

class UserSettingCreate(generics.CreateAPIView):
    serializer_class = UserSettingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


## Calorie-entry CRUD

class CalorieEntryCreateView(generics.CreateAPIView):
    serializer_class = CalorieEntrySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        calorie_entry = serializer.save(user=user)

        # if user doesn't enter calories
        if calorie_entry.calories == None:
            api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
            query = calorie_entry.text
            response = requests.get(api_url + query, headers={'X-Api-Key': 'FAbEo9/+JKPbP/VmU4NUcg==f0YtGPFJYVNXcgSz'})
            data = json.loads(response.content)
            calorie_entry.calories = data['items'][0]['calories']
            calorie_entry.save()

        daily_total_calories = CalorieEntry.objects.filter(
            user=user,
            date=datetime.date.today()
        ).aggregate(total_calories=Sum('calories'))['total_calories']

        # Get the user's expected calories per day
        expected_calories_per_day = user.usersetting.expected_calories_per_day

        # Update the 'is_under_expected_calories' field based on the comparison
        if daily_total_calories <= expected_calories_per_day:
            calorie_entry.is_under_expected_calories = True
            calorie_entry.save()


class CalorieEntryUpdateView(generics.UpdateAPIView):
    serializer_class = CalorieEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CalorieEntry.objects.filter(user=self.request.user)
        return queryset

    def perform_update(self, serializer):
        user = self.request.user
        calorie_entry = serializer.save(user=user)

        # if user doesn't enter calories
        if calorie_entry.calories == None:
            api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
            query = calorie_entry.text
            response = requests.get(api_url + query, headers={'X-Api-Key': 'FAbEo9/+JKPbP/VmU4NUcg==f0YtGPFJYVNXcgSz'})
            data = json.loads(response.content)
            calorie_entry.calories = data['items'][0]['calories']
            calorie_entry.save()

        daily_total_calories = CalorieEntry.objects.filter(
            user=user,
            date=calorie_entry.date
        ).aggregate(total_calories=Sum('calories'))['total_calories']

        # Get the user's expected calories per day
        expected_calories_per_day = user.usersetting.expected_calories_per_day

        # Update the 'is_under_daily_goal' field based on the comparison
        if daily_total_calories <= expected_calories_per_day:
            calorie_entry.is_under_expected_calories = True
        else:
            calorie_entry.is_under_expected_calories = False
        calorie_entry.save()


class CalorieEntryListView(generics.ListAPIView):
    serializer_class = CalorieEntryListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CalorieEntry.objects.filter(user=self.request.user)
        return queryset.order_by('-date', '-time')


class CalorieEntryRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = CalorieEntryListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CalorieEntry.objects.filter(user=self.request.user)
        return queryset
