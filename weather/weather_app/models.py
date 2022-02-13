from django.db import models

class City(models.Model):
    name 	   = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

class WeatherRecord(models.Model):
    city 		= models.ForeignKey(City,on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    temperature = models.CharField(max_length=20, null=True, blank=True)
    icon 	    = models.CharField(max_length=20, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'weather_records'
