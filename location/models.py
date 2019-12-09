from django.db import models

# Create your models here.


class Region(models.Model):
    region = models.CharField(max_length=30)

    def __str__(self):
        return self.region

class City(models.Model):
    region = models.ForeignKey(Region, related_name='RegionCities', on_delete=models.CASCADE)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city



class Neighborhood(models.Model):
    city_id         = models.ForeignKey(City, on_delete=models.CASCADE)    
    neighborhood_name = models.CharField(verbose_name='Neighborhood', max_length=20)
    
    def __str__(self):
        return self.neighborhood_name


