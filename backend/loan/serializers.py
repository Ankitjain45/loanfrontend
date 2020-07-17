
from rest_framework import serializers
from .models import Userdetails

class UserdeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = ('id', 'name', 'email', 'phone', 'aadhar', 'pan', 'address')