#!/usr/bin/python3


"""First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization Constructor
        Args:
            width(int)    :Int
            height(int)   :Int
            x(int)        :Int
            y(int)        :Int
            id(int or None):Int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Return the width attribute as private
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width attribute
        """
        self.__width = value

    @property
    def height(self):
        """
        Return the height attribute as private
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height attribute
        """
        self.__height = value

    @property
    def x(self):
        """
        Return the x attribute as private
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x attribte
        """
        self.__x = value

    @property
    def y(self):
        """
        Return the y attribute as private
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y attribute
        """
        self.__y = value
