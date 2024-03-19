#!/usr/bin/env python3
"""
class for city model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    a class that inherits from BaseModel

    Attributes:
        state_id : string
        name : string
    """

    state_id = ""
    name = ""
