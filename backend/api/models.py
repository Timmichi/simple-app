from django.db import models
from django.contrib.auth.models import User

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies") # A movie is uploaded by a user. If a user is deleted, all movies by that user will be deleted as well. related_name allows us to access notes from a user object.
    director = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self):
        return self.title
