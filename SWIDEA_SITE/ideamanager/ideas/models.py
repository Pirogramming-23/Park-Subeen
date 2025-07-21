# ideas/models.py
from django.db import models
from django.contrib.auth.models import User

class DevTool(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='idea_images/')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name='ideas')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='stars')

    class Meta:
        unique_together = ('user', 'idea')
