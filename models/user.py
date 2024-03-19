#!/usr/bin/env python3
"""
user class model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    a class that inherits from BaseModel

    Attributes:
        email : string - empty string
        password : string - empty string
        first_name : string - empty string
        last_name : string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
