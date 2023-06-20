#!/usr/bin/python3


"""Compare rectangles"""


class Rectangle:
    """Rectangles :s"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    number_of_instances = 0

    print_symbol = "#"

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        i = 0
        while i < self.__height:
            j = 0
            while j < self.__width:
                rectangle += str(self.print_symbol)
                j += 1
            if i == self.__height - 1:
                break
            rectangle += "\n"
            i += 1
        return rectangle

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
