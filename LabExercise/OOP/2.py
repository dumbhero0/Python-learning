#write a python program to create a calculator class. Include methods for basic arithmetic operator
class Calculator:
    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def div(self, a, b):
        return a/b
    
    def mul(self, a, b):
        return a*b
    
calc1=Calculator()
print(calc1.add(5,5))
print(calc1.sub(5,5))
print(calc1.div(5,5))
print(calc1.mul(5,5))
