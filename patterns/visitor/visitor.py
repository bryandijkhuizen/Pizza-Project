# create a visitor interface

class Visitor:
    def __str__(self):
        return self.__class__.__name__