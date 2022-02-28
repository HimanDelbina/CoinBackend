from rest_framework import serializers
from .models import NewsModel


class NewsSerializers(serializers.ModelSerializer):
    queryset = NewsModel.objects.all()

    class Meta:
        model = NewsModel
        fields = '__all__'
