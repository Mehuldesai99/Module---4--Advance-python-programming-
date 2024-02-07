# >>> 21.How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.

"""
a class is a blueprint for creating objects. It encapsulates data (attributes) and functions (methods) that operate on that data. To define a class in Python, you use the class keyword followed by the class name and a colon.

class MyClass:
    pass  # Placeholder to indicate an empty class
    

self in Python refers to the instance of the class itself. It's a convention (not a keyword) to represent the instance of the class. When defining methods within a class, the self parameter is the first parameter of any instance method and refers to the instance of the class. It allows you to access and modify the attributes and methods of the class within its own scope.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Creating object
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name) 
print(dog2.age)

print(dog1.bark())  
print(dog2.bark())  


"""