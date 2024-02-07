#>>> 23.Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.1416 * self.radius**2  

    def compute_perimeter(self):
        return 2 * 3.1416 * self.radius  

# Creating an instance of the Circle class
circle = Circle(5)

# Computing the area and perimeter of the circle
area = circle.compute_area()
perimeter = circle.compute_perimeter()

print(f"The area of the circle is: {area:.2f} square units")
print(f"The perimeter of the circle is: {perimeter:.2f} units")
