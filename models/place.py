#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    attribute:
        city_id : The City id.
        user_id : The User id.
        name : The name
        description : The description
        number_rooms : The number rooms
        number_bathrooms : The number bathrooms
        max_guest : The  number of guests
        price_by_night : The price by night
        latitude : The latitude
        longitude : The longitude
        amenity_ids : A Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
