from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import WallModel
from .serializers import WallSerializers
# Create your views here.


@api_view(['GET'])
# @permission_classes([AllowAny])
def get_wall(request):
    wall = WallModel.objects.all()
    ser = WallSerializers(wall, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)
