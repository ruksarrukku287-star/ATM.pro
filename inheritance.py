
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Addition(Calculator):
    def add(self):
        return self.a + self.b
    
class Subtraction(Calculator):
    def subtract(self):
        return self.a - self.b
    
class Multiplication(Addition):
    def multiply(self):
        return self.a * self.b

class Division(Subtraction, Multiplication):
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error! Division by zero."
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

calc = Division(a, b)

print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())

