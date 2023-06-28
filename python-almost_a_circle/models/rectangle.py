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
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method public, that returns the area value of instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Method public, which prints to stdout the instance of
        Rectangle with the character "#"
        """
        for yt in range(self.__y):
            print()
        for ht in range(self.__height):
            for xt in range(self.__x):
                print(" ", end="")
            for wt in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        User readable string
        """
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        texto = ("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))
        return texto
