from rest_framework import serializers
from django.contrib.auth.models import User


class UserReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser',
                   'is_active', 'groups', 'user_permissions']


class UserWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user

        def update(self, instance, validated_data):
            password = validated_data.pop('password')
            user = super().update(instance, validated_data)
            user.set_password(password)
            user.save()
            return user
