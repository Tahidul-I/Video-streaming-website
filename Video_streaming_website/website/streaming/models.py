from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    video = EmbedVideoField()
    thumbnail = models.ImageField(upload_to='thumbnail',blank=True,null=True)

    def __str__(self):
        return self.name
    

class comment(models.Model):
    content = models.ForeignKey(Item, on_delete=models.CASCADE,blank=True,null=True,related_name ='user_comments' )
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    commented = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
