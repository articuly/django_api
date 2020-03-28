from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
