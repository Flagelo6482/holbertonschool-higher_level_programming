#!/usr/bin/python3


"""And now, the Square!"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor Method
        Args:
            size(int)       :Int
            x(int)          :Int
            y(int)          :Int
            id(int or None) :Int or None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        User readable string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Return width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the value of the variable
        Args:
            value(int) :Int
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
