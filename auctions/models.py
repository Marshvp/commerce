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
                listing_current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
                created_at = models.DateTimeField(auto_now_add=True)
                updated_at = models.DateTimeField(auto_now=True)
                watchlisted_users = models.ManyToManyField(User, blank=True, related_name="watchlist")
                winner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="won_auctions")
                # Status
                STATUS_CHOICES = [
                    ('active', 'Active'),
                    ('closed', 'Closed'),
                    ('pending', 'Pending'),
                ]
                status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')


                def __str__(self):
                    return self.listing_title
                
                def determine_winner(self):
                    # Check if there are any bids for this listing
                    if self.bids.exists():
                        # Get the highest bid
                        highest_bid = self.bids.order_by('-buyer_bid').first()

                            # Return the user who made the highest bid
                        return highest_bid.user

                    return None
                


class Comments(models.Model):
                user = models.ForeignKey(User, on_delete=models.CASCADE)
                listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
                comment_contents = models.TextField()
                created_at = models.DateTimeField(auto_now_add=True)

                def __str__(self):
                    return f"{self.user.username} - {self.listing.listing_title} - {self.created_at}"

class Bids(models.Model):
                user = models.ForeignKey(User, on_delete=models.CASCADE)
                listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
                buyer_bid = models.DecimalField(max_digits=10, decimal_places=2)
                created_at = models.DateTimeField(auto_now_add=True)

                def __str__(self):
                    return f"{self.user.username} - {self.listing.listing_title} - {self.buyer_bid}"
'''



class bids()




class comments()
'''