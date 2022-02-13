from rest_framework import serializers
from rest_framework_bulk.drf3.serializers import BulkSerializerMixin, BulkListSerializer

from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class WeatherRecordsSerializer(serializers.ModelSerializer):
	class Meta:
		model = WeatherRecord
		fields = '__all__'
