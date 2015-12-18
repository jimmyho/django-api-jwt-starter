__author__ = 'jimmy'
from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import User
from django.contrib.auth.models import Group

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url',
                  'name')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email',
                  'name', 'date_joined', 'password',
                  'confirm_password', 'groups')
        read_only_fields = ('date_joined',)

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            # instance.username = validated_data.get('username', instance.username)
            # instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance

