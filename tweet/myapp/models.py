from django.db import models
from django.contrib.auth.models import User

class tweet(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=100)
    photo=models.ImageField(upload_to='photos/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def email(self):
        return self.name.email
    
    def id(self):
        return self.name.id
