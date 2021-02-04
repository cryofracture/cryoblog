from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    # 1 author can write many posts.
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE,)
    title = models.CharField(max_length=100) # A title for the blog post/article.
    date = models.DateTimeField(default=datetime.now()) # Sets the date at time of posting for chronological organization
    body = models.TextField() # You know.
    def __str__(self):
        return self.title
