from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import requests
import json
from .serializers import UserSerializer
from .models import Role, Profile
from coin import settings
from django.contrib.auth import authenticate
import random
from django.db import transaction

# import pandas as pd


@transaction.atomic
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    ser = UserSerializer(data=request.data)

    if ser.is_valid():
        ser.save()
        u = update_profile(request)
        user = User.objects.filter(username=ser.data["username"]).first()
        token = Token.objects.create(user=user)
        h = ser.data
        h.update(u)
        h["token"] = token.key
        h["password"] = " "

        return Response(h, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


def update_profile(request):
    user = User.objects.get(username=request.data["username"])
    user.profile.phone_number = request.data["phone_number"]
    user.profile.fcm_token = request.data["fcm_token"]
    role = Role.objects.filter(pk=request.data["role"]).first()
    user.profile.role = role
    user.save()
    return request.data


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    u = authenticate(
        username=request.data["username"], password=request.data["password"])
    if u is not None:
        user = User.objects.filter(username=request.data["username"])
        h = {}
        token = Token.objects.filter(user=user[0])
        p = Profile.objects.filter(user=user[0])[0]

        h["token"] = str(token.first())
        h["username"] = user[0].username
        h["first_name"] = user[0].first_name
        h["last_name"] = user[0].last_name
        h["role"] = str(p.role)
        h["phone_number"] = p.phone_number
        h["fcm_token"] = p.fcm_token
        return Response(h, status=status.HTTP_200_OK)
    else:
        h = {}
        h["message"] = "اطلاعات ورودی اشتباه است"
        return Response(h, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def check_token(request):
    token = request.data['token']
    if request.data['token'] == "":
        h = {}
        h["message"] = "کاربر ثبت نام نکرده"
        return Response(h, status=status.HTTP_404_NOT_FOUND)
    else:
        user_token = Token.objects.filter(key=token)
        user_id = user_token.values()[0]['user_id']
        user = Profile.objects.filter(pk=user_id)
        if len(user) > 0:
            h = {}
            h["role"] = str(user[0].role)
            return Response(h, status=status.HTTP_200_OK)
        else:
            h = {}
            h["message"] = "کاربر وجود ندارد"
            return Response(h, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def forget_password(request):
#     # token = request.auth
#     # token = Token.objects.filter(key=token)
#     # user_id = token.values()[0]['user_id']
#     # user = User.objects.filter(id=user_id).first()

#     p = Profile.objects.filter(phone_number=request.data['phone_number']).first()
#     user = p.user
#     phone_number=user.profile.phone_number
#     user_list = []

#     user_list.append(phone_number)
#     new_password = str(random.randint(100000, 999999))
#     txt = 'رمز جدید شما: ' + new_password
#     url = "http://87.107.121.52/post/sendsms.ashx?from=50002237171&to="+str(user_list)+"&text="+str(txt)+"&password=nim@123@nim&username=westco"
#     r = requests.post(url)
#     user = User.objects.filter(username=user).first()
#     if r.status_code == 200:
#         user.set_password(new_password)
#         user.save()


#     print("*********************************")
#     print("*********************************")
#     print("*********************************")
#     print("new_password: ",new_password)
#     return Response({"message":"رمز با موفقیت بازنشانی شد"}, status = status.HTTP_200_OK)


# @api_view(['POST'])
# def change_password(request):
#     data = request.data
#     token = request.auth
#     token = Token.objects.filter(key=token)
#     user_id = token.values()[0]['user_id']
#     user = User.objects.filter(id=user_id).first()
#     if data["password1"]==data["password2"]:
#         user.set_password(data["password1"])
#         user.save()
#         return Response({"message":"تغییر رمز با موفقیت انجام شد."}, status = status.HTTP_200_OK)
#     else:
#         return Response({"message":""}, status = status.HTTP_200_OK)
