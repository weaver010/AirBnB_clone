#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
       attribute:
           state_id : The state id.
           name : The name
       """

    state_id = ""
    name = ""
