#!/usr/bin/python3
'''Module of Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a formatted string representation."""
        return '[Square] ({}) {}/{} - {}'.\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
