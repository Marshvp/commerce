from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
                listing_title = models.CharField(max_length=255)
                listing_description = models.TextField()
                listing_current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=None)
                listing_starting_price = models.DecimalField(max_digits=10, decimal_places=2)
                seller = models.ForeignKey(User, on_delete=models.CASCADE)

                created_at = models.DateTimeField(auto_now_add=True)
                updated_at = models.DateTimeField(auto_now=True)
                
                # Status
                STATUS_CHOICES = [
                    ('active', 'Active'),
                    ('closed', 'Closed'),
                    ('pending', 'Pending'),
                ]
                status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

                def __str__(self):
                    return self.listing_title
'''



class bids()




class comments()
'''