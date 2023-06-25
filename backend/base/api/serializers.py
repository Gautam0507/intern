from rest_framework.serializers import ModelSerializer
from base.models import Meter


class MeterSerializer(ModelSerializer):
    class Meta:
        model = Meter
        fields = '__all__'
