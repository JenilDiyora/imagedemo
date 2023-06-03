from rest_framework import serializers
from imgapi.models import Profile
from drf_extra_fields.fields import Base64ImageField
# import os
# import base64
# import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
      pimage=Base64ImageField()
      class Meta:
         model=Profile
         fields= ['id','name','email','dob','state','gender','location','pimage']
      def create(self, validated_data):
        name=validated_data.pop('name')
        email=validated_data.pop('email')
        dob=validated_data.pop('dob')
        state=validated_data.pop('state')
        gender=validated_data.pop('gender')
        location=validated_data.pop('location')
        pimage=validated_data.pop('pimage')
        return Profile.objects.create(name=name,email=email,dob=dob,state=state,gender=gender,location=location,pimage=pimage)


# class ProfileSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = Profile
#                 fields = ['id','name','email','dob','state','gender','location','pimage']


