from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import CreateUser


class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['expiry'] = int(refresh.access_token.lifetime.total_seconds())
        return data


class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['expiry'] = int(refresh.access_token.lifetime.total_seconds())
        return data


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, min_length=8
    )

    class Meta:
        model = CreateUser
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate_username(self, value):
        query = CreateUser.objects.filter(username=value)

        if self.instance:
            query = query.exclude(id=self.instance.id)
        if query.exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        user = self.instance
        if (
            user
            and CreateUser.objects.filter(email=value)
            .exclude(id=user.id)
            .exists()
        ):
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):

        user = CreateUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')

        print(validated_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
