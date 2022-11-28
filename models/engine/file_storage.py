#!/usr/bin/python3

"""A module that contains attributes
and methods for serialisation and
deserialization of JSON data"""
import datetime
import models
import json
import os


def models_encod_hook(obj):
    """Returns an instance of a generated json string literal"""
    try:
        cls = obj['__class__']
    except KeyError:
        return obj
    else:
        try:
            return getattr(models, cls)(**obj)
        except AttributeError:
            return obj


class FileStorage:
    """serializes instances to a
    JSON file & deserializes back
    to instances"""

    # string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """Return all the objects saved in the file"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serialises __objects to the JSON file"""
        json_objects = {}
        filename = FileStorage.__file_path
        for keys in FileStorage.__objects:
            json_objects[keys] = FileStorage.__objects[keys].to_dict()
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        filename = FileStorage.__file_path
        if not os.path.isfile(filename):
            return
        with open(filename, mode='r', encoding='utf-8') as rf:
            FileStorage.__objects = json.load(rf, object_hook=models_encod_hook)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review}
        return class_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"Place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
