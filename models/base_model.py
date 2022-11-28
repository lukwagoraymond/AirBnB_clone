#!/usr/bin/python3
"""A module that defines all common
attributes/methods for other classes
"""
import models
from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Represents a BaseModel Class
    Args:
        - *args: list of arguments
        - **kwargs: dict of key-value pair arguments
    """

    def __init__(self, *args, **kwargs):
        """Initialisation Method"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of a class"""
        cls_name = self.__class__.__name__
        cls_dict = str(self.__dict__)
        return "[{:s}] ({:s}) {:s}".format(cls_name, self.id, cls_dict)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        if "created_at" in dict_copy:
            dict_copy['created_at'] = dict_copy['created_at'].strftime(time)
        if "updated_at" in dict_copy:
            dict_copy['updated_at'] = dict_copy['updated_at'].strftime(time)
        return dict_copy
