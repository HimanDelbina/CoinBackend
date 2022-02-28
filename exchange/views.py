from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from exchange.models import ExchangeModel
from exchange.serializers import ExchangeSerializers

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_exchange_list(request):
    news_types = ExchangeModel.objects.all()

    ser = ExchangeSerializers(news_types, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)
