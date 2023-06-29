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

    def update(self, *args, **kwargs):
        """
        Assign values according to the arguments of "*args" and "**kwargs"
        Args:
            *args(tuple)  :Tuple
            **kwargs(dict):Diccionary
        """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Function that returns the dictionary of class "Square"
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
