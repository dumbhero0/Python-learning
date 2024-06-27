#Write a program to create a class representing a circle, include methods to calculate its area and perimeter.
class Circle:
    def area(self, a):
        return 3.14*a*a
    
    def perimeter(self, a):
        return 2*3.14*a
    


circle1=Circle()
print(circle1.area(5))
print(circle1.perimeter(5))