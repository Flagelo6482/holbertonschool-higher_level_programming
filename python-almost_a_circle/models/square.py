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
