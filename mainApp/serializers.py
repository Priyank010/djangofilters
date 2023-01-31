from mainApp.models import *
from rest_framework import serializers

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'