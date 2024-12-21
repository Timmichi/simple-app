from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView): # ListCreateAPIView is a generic view that provides GET (list) and POST method handlers. In this case, it will list all notes when a GET request is made to the view, and create a new note object when a POST request is made to the view.
    serializer_class = NoteSerializer # The serializer class we want to use
    permission_classes = [IsAuthenticated] # Only authenticated users can access this view. We require authentication to create a note.

    # We are overriding the get_queryset method to filter the notes based on the user making the request.
    def get_queryset(self):
        user = self.request.user # The user making the request
        return Note.objects.filter(author=user)
    
    # We are overriding the perform_create method to set the author field of the note to the user making the request.
    def perform_create(self, serializer):
        if serializer.is_valid():
          serializer.save(author=self.request.user) # We have overridden the perform_create method to set the author field of the note to the user making the request.
        else:
          print(serializer.errors)

class NoteDelete(generics.DestroyAPIView): # DestroyAPIView is a generic view that provides DELETE method handler. In this case, it will delete a note object when a DELETE request is made to the view.
   serializer_class = NoteSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
      user = self.request.user
      return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView): # CreateAPIView is a generic view that provides POST method handler. In this case, it will create a new user object when a POST request is made to the view.
    queryset = User.objects.all() # All our users
    serializer_class = UserSerializer # The serializer class we want to use
    permission_classes = [AllowAny] # Allows anyone to create a user. We don't want to require authentication to create a user.
