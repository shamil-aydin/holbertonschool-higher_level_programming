#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__size

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # and considering its position."""
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (y-axis)
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Print the square rows
        for _ in range(self.__size):
            # Print horizontal offset (x-axis)
            print(" " * self.__position[0], end="")
            # Print the square itself
            print("#" * self.__size)
