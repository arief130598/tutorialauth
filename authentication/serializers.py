from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
