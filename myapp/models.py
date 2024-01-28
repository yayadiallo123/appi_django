from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.name
    image = models.ImageField(upload_to='Images',default="Images/None/seample.jpg")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    rating = models.FloatField()