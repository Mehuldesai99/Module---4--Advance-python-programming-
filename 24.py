#>>> 24. Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

"""
Inheritance in Python allows a new class (subclass) to inherit properties (methods and attributes) from an existing class (superclass). This concept facilitates code reusability and enables the creation of a hierarchy of classes where subclasses can access and extend the functionality of their parent class.

# Parent class (superclass)
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Placeholder method to be overridden in subclasses

# Subclass inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__('Dog')  # Calling parent class constructor
        self.name = name
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Creating an instance of the subclass
my_dog = Dog('Buddy', 'Labrador')

# Accessing attributes and methods from the superclass and subclass
print(f"My {my_dog.species} {my_dog.name} ({my_dog.breed}) says {my_dog.make_sound()}")


In Python, __init__ is a special method (also known as a constructor) that gets called automatically when an object of a class is instantiated. It initializes the object's attributes or performs any necessary setup required for the object.

In the context of the example above, the __init__ method in both Animal and Dog classes is a constructor used to initialize the attributes (species, name, breed) of instances created from these classes.
The super().__init__() line in the subclass constructor (Dog) calls the constructor of the superclass (Animal) to initialize the species attribute.
It's a convention in Python to use __init__ as a constructor method, but it's not mandatory to have one in every class.
"""