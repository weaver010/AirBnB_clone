#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
      attribute:
          place_id : The Place id.
          user_id : The User id.
          text : The text
      """

    place_id = ""
    user_id = ""
    text = ""
