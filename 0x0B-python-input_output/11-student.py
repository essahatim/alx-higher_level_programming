#!/usr/bin/python3
'''Module of the student class'''


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        json_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                json_dict[key] = value
        return json_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with the values from the given dictionary
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
