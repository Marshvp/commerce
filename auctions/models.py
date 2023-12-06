from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
                listing_title = models.CharField(max_length=255)
                listing_description = models.TextField()
                listing_image_url = models.URLField(blank=True, null=True)
                listing_starting_price = models.DecimalField(max_digits=10, decimal_places=2)
                seller = models.ForeignKey(User, on_delete=models.CASCADE)
                listing_category = models.CharField(max_length=255, blank=True, null=True)

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