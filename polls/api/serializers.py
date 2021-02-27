from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import SerializerMethodField, empty
from polls.models import *
from django.utils import timezone
import datetime
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__" 
class SignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 50)
    last_name = serializers.CharField(max_length = 50)
    email = serializers.EmailField()
    class Meta:
        model= User
        fields = "__all__"
class UserPrettySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["username", "first_name", "last_name", "email", "id"]