#>>> 26.What is used to check whether an object o is an instance of class A?

"""
In Python, you can use the isinstance() function to check whether an object is an instance of a particular class.

class A:
    pass

obj = A()
result = isinstance(obj, A)
print(result) 

he isinstance() function takes two parameters: the object you want to check (obj in this case) and the class or type you want to check against (A in this case). It returns True if the object is an instance of the specified class, and False otherwise.


"""