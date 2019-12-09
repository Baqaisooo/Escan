from django.db import models
from django.contrib.auth.models import AbstractUser
from location.models import Region, City, Neighborhood

 
class User(AbstractUser):
    phone   = models.BigIntegerField(null=True)
    region  = models.ForeignKey(Region, related_name='UserRegion', on_delete=models.CASCADE, null=True)
    city    = models.ForeignKey(City, related_name='UserCity', on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

# Create your models here.
