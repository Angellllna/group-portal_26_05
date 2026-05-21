from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()              
    publication_date = models.DateTimeField(auto_now_add=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    is_important = models.BooleanField(default=False)          

    def __str__(self):
        return self.title