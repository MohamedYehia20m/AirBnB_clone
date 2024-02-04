#!/usr/bin/python3
"""State module"""

from models.base_model import BaseModel

class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of State instance"""
        super().__init__(*args, **kwargs)
