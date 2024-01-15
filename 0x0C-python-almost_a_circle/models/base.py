#!/usr/bin/python3
'''Module of a Base Class'''


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
