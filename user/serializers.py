from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Profile, Role


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'password')
        extra_kwargs = {'password': {"write_only": True, "required": True, }}

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(validated_data['password'])
        user.save()
        user.password = password
        # user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('role', 'phone_number', 'fcm_token')

        depth = 1


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


# class AccessLevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccessLevel
#         fields = "__all__"


# class AccessLevelGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccessLevelGroup
#         fields = "__all__"
#         depth = 2


# class UserAccessLevelGroupSerializer(serializers.ModelSerializer):
#     access_level = AccessLevelSerializer()

#     class Meta:
#         model = UserAccessLevelGroup
#         fields = "__all__"
