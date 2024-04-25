from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Forecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.city}: {self.date} - Max: {self.max_temperature}, Min: {self.min_temperature}"