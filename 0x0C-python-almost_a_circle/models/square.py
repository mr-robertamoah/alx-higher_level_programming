#!/usr/bin/python3

"""
Contains a Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Base with a __init__ method """

    def __init__ (self, size, x=0, y=0, id=None):
        """
        initializing class or instance attributes

        Args:
            id (int): an integer assignable to self.id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return a string representation of this instance """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

