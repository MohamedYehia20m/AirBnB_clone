#!/usr/bin/python3
"""Amenity module"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity instance"""
        super().__init__(*args, **kwargs)
