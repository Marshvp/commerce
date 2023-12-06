from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ListingForm, BidForm
from django.contrib import messages

from .models import User, Listing, Bids


def index(request):
    active_listings = Listing.objects.filter(status='active')
    return render(request, "auctions/index.html", {'active_listings': active_listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.seller = request.user
            new_listing.save()
            return redirect('index')
    else:
        form = ListingForm()

    return render(request, 'auctions/create_listing.html', {'form': form})



def listing_page(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)
    comments = listing.comments.all()
    bids = listing.bids.all()

    return render(request,'auctions/listing_page.html', {'listing':listing, 'comments':comments, 'bids':bids})




def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    bids = listing.bids.all()

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            buyer_bid = form.cleaned_data['buyer_bid']

            # Check if the new bid is greater than the current price
            if buyer_bid > listing.listing_current_price:
                # Create a new bid
                bid = Bids(user=request.user, listing=listing, buyer_bid=buyer_bid)
                bid.save()

                # Update the current price
                listing.listing_current_price = buyer_bid
                listing.save()

                messages.success(request, 'Bid placed successfully.')
                return redirect('listing_page', listing_id=listing_id)
            else:
                messages.error(request, 'Bid must be greater than the current price.')

    else:
        form = BidForm()

    return render(request, 'auctions/listing_page.html', {'listing': listing, 'form': form, 'bids': bids})