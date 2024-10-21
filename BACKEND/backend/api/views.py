from django.shortcuts import render
from userauths.models import User
from api import serializers as api_serializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=api_serializer.MyTokenObtainPairSerailizer

class RegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = [AllowAny]

    serializer_class=api_serializer.RegisterSerializer