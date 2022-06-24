from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



DISTANCES = (
    ('S', 'Short Walk'),
    ('L', 'Long Walk'),
    ('F', 'Fly'),
    ('N', 'Swim'),
)

ENVIRONMENTS = (
    ('C', 'Cities'),
    ('F', 'Forests'),
    ('L', 'Lakes'),
    ('M', 'Mountains'),
    ('O', 'Oceans'),
    ('R', 'Rivers'),
    ('U', 'Underground'),
)


# Create your models here.

# LOCATION Model

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    environment = models.CharField(max_length=1, choices=ENVIRONMENTS, default=ENVIRONMENTS[0][0])
    image = models.URLField(max_length=500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'pk': self.id})



# BEAST Model

class Beast(models.Model):
    name = models.CharField(max_length=100)
    native = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    size = models.CharField(max_length=100)
    danger = models.PositiveSmallIntegerField()
    image = models.URLField(max_length=500)
    locations = models.ManyToManyField(Location)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('beast_detail', kwargs={'beast_id': self.id})

    class Meta:
        ordering = ['name']

    def exercised_today(self):
        return self.walk_set.filter(date=date.today()).count() >= 1



# WALK Model

class Walk(models.Model):
    date = models.DateField("Exercise Date")
    distance = models.CharField(max_length=1, choices=DISTANCES, default=DISTANCES[0][0])
    beast = models.ForeignKey(Beast, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_distance_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

