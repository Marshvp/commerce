from django.urls import path
from . import views
from .views import create_listing, listing_page, place_bid


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create_listing/', create_listing, name='create_listing'),
    path('listing/<int:listing_id>/', listing_page, name='listing_page'),
    path('place_bid/<int:listing_id>/', place_bid, name='place_bid'),
]
