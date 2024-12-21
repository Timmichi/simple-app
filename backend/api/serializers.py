from django.contrib.auth.models import User # uses ORM to interact with the database
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # We want to accept password when creating a user, but we don't want to return it when giving information about a user. No one can read the password.
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # **extra_fields will unpack a dictionary into keyword arguments.For example, if extra_fields is {'is_active': True, 'age': 30}, then **extra_fields will pass is_active=True and age=30 as keyword arguments to the _create_user method.
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"] # Include specific fields in the serializer
        extra_kwargs = {"author": {"read_only": True}} # The author field should not be modified by the user. It will be set automatically by us (backend) when the note is initially created.