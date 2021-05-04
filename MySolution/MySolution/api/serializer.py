from rest_framework import serializers
from .models import Courses


# Providing way for serializing of our model into JSON
class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
