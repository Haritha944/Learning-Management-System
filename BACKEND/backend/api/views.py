from django.shortcuts import render
from userauths.models import User
from api import serializers as api_serializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics,status
from rest_framework.response import Response
import random

# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=api_serializer.MyTokenObtainPairSerailizer

class RegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = [AllowAny]

    serializer_class=api_serializer.RegisterSerializer



def generate_random_otp(Length=7):
    otp=''.join([str(random.randint(0,9)) for _ in range(Length)])
    return otp
class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = api_serializer.Userserializer

    def get_object(self):
        email=self.kwargs['email']
        user=User.objects.filter(email=email).first()
        if user:
            uuidb64=user.pk
            refresh=RefreshToken.for_user(user)
            refresh_token=str(refresh.access_token)
            user.refresh_token=refresh_token
            user.otp=generate_random_otp()
            user.save()
            link= f"http://localhost:5173/create-new-password/?otp={user.otp}&uuidb64={uuidb64}&=refresh_token={refresh_token}" 
            print("link____",link)                                                        
        return user
    
class PasswordChangeAPIView(generics.CreateAPIView):
    permission_classes= [AllowAny]
    serializer_class=api_serializer.Userserializer
    def create(self,request,*args,**kwargs):
        payload=request.data
        otp=payload['otp']
        uuidb64 = payload['uuidb64']
        password=payload['password']

        user = User.objects.get(id=uuidb64,otp=otp)
        if user:
            user.set_password(password)
            user.otp=""
            user.save()
            return Response({"message":"Password changed sucessfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"User not exists"},status=status.HTTP_404_NOT_FOUND)