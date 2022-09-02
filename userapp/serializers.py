from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'mobile_no', 'first_name', 'last_name', 'password']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()