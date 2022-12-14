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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) == 0:
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        if type(v) == str:
                            v = datetime.strptime(v, time)
                        else:
                            if k == 'created_at':
                                v = self.created_at
                            elif k == 'updated_at':
                                v = self.updated_at
                    if k == 'id':
                        v = str(v)
                    setattr(self, k, v)
                if k == 'id':
                    existing = models.storage.all()
                    id_str = self.__class__.__name__ + '.' + str(v)
                    if id_str not in existing.keys():
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
            dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        if "updated_at" in dict_copy:
            dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
