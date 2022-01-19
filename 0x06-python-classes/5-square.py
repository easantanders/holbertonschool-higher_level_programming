#!/usr/bin/python3


" A class Square that defines a sixe for a square "


class Square:
    """
    Square class
    Attributes:
        size (int) : Private attribute
    """
    __size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """
    Public instance method that returns the current square area

    """
    def area(self):
        return self.size ** 2
    """
    Public instance method that print square with "#"

    """
    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.size):
                print("#", end="")
            print("")
