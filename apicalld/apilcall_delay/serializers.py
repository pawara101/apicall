## To convert the Model object to an API-appropriate format like JSON, Django REST framework uses the ModelSerializer class to convert any model to serialized JSON objects
from rest_framework import serializers
from .models import Apicall


class ApicallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apicall
        # fields = ["task", "completed", "timestamp", "updated", "user"]