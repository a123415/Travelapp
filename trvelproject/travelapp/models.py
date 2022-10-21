from django.db import models

# Create your models here.
class design(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos')
    desc = models.TextField()

    def __str__(self):
        return self.name
