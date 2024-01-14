#!/usr/bin/python3
"""Defines the User class."""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
       attribute:
           email : The email
           password : The password
           first_name : The first name
           last_name : The last name
       """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
