from django.urls import path
from . import views
from .views import create_listing, listing_page, place_bid, watchlist_page, watchlist_btn, add_comment,close_auction


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create_listing/', create_listing, name='create_listing'),
    path('listing/<int:listing_id>/', listing_page, name='listing_page'),
    path('place_bid/<int:listing_id>/', place_bid, name='place_bid'),
    path('watchlist/', watchlist_page, name='watchlist_page'),
    path('watchlist_btn/<int:listing_id>/', watchlist_btn, name='watchlist_btn'),
    path('add_comment/<int:listing_id>/',add_comment, name='add_comment'),
    path('close_auction/<int:listing_id>/', close_auction, name='close_auction'),

]
