from django.db import models

# Create your models here.
class Trip(models.Model):
    trip_name = models.CharField(max_length=100)
    trip_duration = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.trip_name
    
class ExpenseTracker(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to="trips_img/",null=True)
    files = models.FileField(upload_to="trips_file//",null=True)
    
    def __str__(self):
        return self.title