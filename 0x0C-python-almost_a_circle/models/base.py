#!/usr/bin/python3
'''Module of a Base Class'''
import json


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """The list of dictionaries from the JSON string representation."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is not None:
            list_objes = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        from models.rectangel import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_instance = Rectangle(1, 1)
        elif cls is Square:
            new_instance = Square(1)
        else:
            new_instance = None
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        from os import path
        file = '{}.json'.format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            json_string = f.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]
