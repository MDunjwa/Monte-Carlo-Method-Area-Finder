import math

class Shape:

    def __init__(self,width=0,height=0,diameter=0,radius1=0,radius2=0):
        self.width = width
        self.height = height
        self.radius_one = radius1
        self.radius_two = radius2
        self.diameter = diameter

    def find_area(self):
        pass

    def circle_area(self):
        return math.pi * ((self.diameter/2)**2)
    
    def square_area(self):
        return self.width**2
    
    def rectangle_area(self):
        return self.width * self.height 
    
    def ellipse_area(self):
        return math.pi * self.radius_one * self.radius_two
    
s = Shape(diameter=5)
print(s.circle_area())
    


