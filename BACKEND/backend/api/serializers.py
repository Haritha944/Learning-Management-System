from rest_framework import serializers
from userauths.models import Profile,User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'