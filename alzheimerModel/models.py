from django.db import models

# Create your models here.

class Alzheimer(models.Model):
    name = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to = 'images/') #by default django creates the directory under media