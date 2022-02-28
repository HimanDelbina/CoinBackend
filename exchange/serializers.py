from rest_framework import serializers
from .models import ExchangeModel


class ExchangeSerializers(serializers.ModelSerializer):
    queryset = ExchangeModel.objects.all()

    class Meta:
        model = ExchangeModel
        fields = '__all__'
