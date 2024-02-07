#>>> 28.What relationship is appropriate for Student and Person?

"""
the relationship between a "Student" and "Person" can often be represented using inheritance. Inheritance allows the "Student" class to inherit characteristics and behaviors from the "Person" class, establishing an "is-a" relationship.

For instance:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Creating instances
person = Person("Alice", 30)
person.display_info()

student = Student("Bob", 20, "S12345")
student.display_info()

Here, the Person class is a generic class that holds attributes common to individuals, such as name and age. The Student class inherits from Person, acquiring these attributes and methods, and adds additional attributes like student_id.

This relationship models that a "Student" is a specialized type of "Person" with some extra attributes or behaviors. This way, you can reuse the properties and methods defined in the Person class within the Student class while adding specific functionalities for students.
"""
