from rest_framework import serializers
from .models import WallModel


class WallSerializers(serializers.ModelSerializer):
    queryset = WallModel.objects.all()

    class Meta:
        model = WallModel
        fields = '__all__'
