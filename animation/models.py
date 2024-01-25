import datetime
from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField("Title", max_length=100)
    image = models.ImageField(upload_to="animation/images/")
    description = models.TextField("Description")
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.title