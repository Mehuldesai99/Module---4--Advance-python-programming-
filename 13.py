#>>> 13. Explain Exception handling? What is an Error in Python?

"""

Exception handling is a programming concept that deals with managing unexpected or exceptional situations that occur during the execution of a program. In Python, exceptions are raised when an error occurs during the execution of a program. Exception handling allows you to gracefully handle these errors, preventing the program from crashing and providing a way to recover or handle exceptional situations.

An error in Python refers to any unexpected situation that prevents the normal flow of a program. Errors in Python are categorized into two main types: syntax errors and exceptions.

1.Syntax Errors: These errors occur when the Python interpreter encounters code that does not follow the correct syntax rules of the language. Syntax errors are detected during the parsing of the code and prevent the program from running. For example, missing colons at the end of a conditional statement or a mistyped keyword can lead to syntax errors.

Syntax Error example
if x == 5  
    print("x is 5")


2.Exceptions: Unlike syntax errors, exceptions occur during the execution of a program (runtime) and can be caused by various reasons such as invalid input, division by zero, file not found, trying to access an index that doesn't exist in a list, and more. When an exceptional condition occurs, an exception is raised, which can interrupt the normal flow of the program.

Python provides a built-in mechanism for handling exceptions using try, except, else, finally, and raise statements:

try: It defines a block of code where exceptions might occur.
except: It catches and handles specific exceptions that occur within the try block.
else: It executes code when no exceptions are raised within the try block.
finally: It defines a block of code that will always be executed, whether an exception occurs or not.
raise: It explicitly raises an exception.

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("No exceptions occurred")
finally:
    print("Finally block executed")


"""