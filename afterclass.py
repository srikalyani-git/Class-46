from abc import ABC, abstractmethod
class shape():
    def area(self):
        pass

class square(shape):
    def __init__(self,side):
        self.side = int(side)
    
    def area(self):
        print(self.side**2, "units^2 is the area of this square")

class triangle(shape):
    def __init__(self, base, height):
        self.base = int(base)
        self.height = int(height)

    def area(self):
        print(0.5 * self.base * self.height, "units^2 is the area of this triangle")

triangle1 = triangle(5,7)
triangle1.area()
square1 = square(8)
square1.area()
