from rest_framework import serializers
from userauths.models import Profile,User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class MyTokenObtainPairSerailizer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        token['full_name']= user.full_name
        token['email']=user.email
        token['username']=user.username
        return token
    
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User
        fields=['full_name','email','password','password2']
    def validate(self,attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError({'password':"passwor fields didnt match"})
        return attr
    def create(self,validated_data):
        user=User.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
                )
        email_username=user.email.split("@")
        user.username=email_username
        user.set_password(validated_data['password'])
        user.save()
        return user
