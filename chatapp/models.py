from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.html import format_html


class TextMessage(models.Model):
     receiver = models.ForeignKey(User, related_name='Receiver', on_delete=models.CASCADE)
     sender = models.ForeignKey(User, related_name='Sender', on_delete=models.CASCADE)
     message = models.TextField()
     sent_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return format_html("<b>From:</b>"+self.sender.username+"<br><b>To:</b>"+self.receiver.username)