from django.db import models
from django.contrib.auth.models import User

# tells Django how to work with the data that will be stored in the app model = class
class Topic(models.Model):
    """a topic we are learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
        
    
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    topic_Img = models.ImageField(upload_to='topic_images/')
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model"""
        return self. text[:50] + "..."