#class name triangle , a b c sides . two functions(perimeter , area)
import math
class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        p = self.a+self.b+self.c
        return p
    def area(self):
        p1 = (self.a+self.b+self.c)/2
        ar = p1*(p1-self.a)*(p1-self.b)*(p1-self.c)
        return math.sqrt(ar)

t = triangle(4,3,2)
t1 = t.perimeter()
t2 = t.area()
print("The perimeter of the triangle is: ",t1)
print("The area of the triangle is: ",t2)
