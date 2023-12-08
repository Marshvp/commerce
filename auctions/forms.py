from django import forms
from .models import Listing, Bids, Comments

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['listing_title', 'listing_description', 'listing_starting_price', 'listing_image_url', 'listing_category']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bids
        fields = ['buyer_bid']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_contents']