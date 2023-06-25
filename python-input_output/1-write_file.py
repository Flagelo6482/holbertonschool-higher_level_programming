#!/usr/bin/python3


"""Write to a file"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        """
        Args:
            filename(file)  :File text
            mode(mode)      :Opening mode
            encoding(coding):Encoding mode
        """
        return file.write(text)
