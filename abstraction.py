from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(s):
        pass
class triangle(shape):
    def area(self):
        print("area of triangle=1/2*b*h")
r=triangle()
r.area()
class square(shape):
    def area(self):
        print("area of square=s*s")
s=square()
s.area()





              
