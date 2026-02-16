from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserProfileSerializer(self.user)
        data.update(user_serializer.data)
        return data