from django.db import models

# Create your models here.

class Product(models.Model):
    discount_choice = (('yes', 'yes'), 
                    ('no', 'no'))
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    stock = models.IntegerField()
    discount = models.CharField(max_length=100, choices=discount_choice)

    def __str__(self):
        return(self.name)