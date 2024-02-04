#!/usr/bin/python3
"""Module for BaseModel class"""

import uuid
import datetime

class BaseModel:
    """
    Class that defines all common attributes/methods for other classes.

     Attributes:
        id (int): Identity of each instance.
        create_at (datetime): Date of each instaance has been created at.
        updated_at (datetime): Date of each instaance has been updated at.
    """

    def __init__(self, *args, **kwargs):
        """Creates new instances of BaseModel."""
        if not kwargs:
            self.id: str = str(uuid.uuid4())
            self.created_at: datetime = datetime.datetime.now()
            self.updated_at: datetime = datetime.datetime.now()

    def save(self):
        """updates the public instance attribute `updated_at` with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of `__dict__` of the instance."""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = self.created_at.isoformat()
        _dict["update_at"] = self.updated_at.isoformat()
        return _dict

    def __str__(self):
        """string representation of class."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
