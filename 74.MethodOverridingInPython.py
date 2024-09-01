class Shape :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14 * super().area()   # This is called method overriding , here are creating a valid method for the class Circle using the area method made for the class Shape . Yani parent class ke ek method ko
    # call karke usko, use kar child class mein ek method ko define karna.

rec = Shape(45,56)
print(rec.area())

cir = Circle(34)
print(cir.area())