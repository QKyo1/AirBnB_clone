#!/usr/bin/env python3
"""
a class to review model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    a class that inherits from BaseModel

    Attributes:
        place_id : string
        user_id : string
        text : string
    """

    place_id = ""
    user_id = ""
    text = ""
