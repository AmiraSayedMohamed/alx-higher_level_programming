#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 5-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            __size (int): size of the square (1 side).
            __position (tuple): position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2


