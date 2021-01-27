from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE,)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    body = models.TextField()
    def __str__(self):
        return self.title
