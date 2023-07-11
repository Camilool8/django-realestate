from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Property(models.Model):
    TYPE_CHOICES = [
        ('RENT', 'For Rent'),
        ('SALE', 'For Sale'),
    ]

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    image = models.ImageField(upload_to='properties/')
    property_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='SALE')
    is_featured = models.BooleanField(choices=((True, 'Yes'), (False, 'No')), default=False)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    logo = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.name
