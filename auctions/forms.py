from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['listing_title', 'listing_description', 'listing_starting_price', 'listing_image_url', 'listing_category']