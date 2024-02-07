# >>> 14.How many except statements can a try-except block have? Name Some built-in exception classes:

"""
A try-except block in Python can have multiple except clauses to handle different types of exceptions that may arise within the try block. Each except clause can handle a specific exception, allowing you to handle different types of errors gracefully.

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    # Handle the ValueError
    print("Please enter a valid number.")
except ZeroDivisionError:
    # Handle the ZeroDivisionError
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", e)


1.except ValueError: Handles the ValueError that might occur when trying to convert input to an integer.

2.except ZeroDivisionError: Handles the ZeroDivisionError that occurs if the user enters zero as the input for division.

3.except Exception as e: Acts as a catch-all for other exceptions that are not explicitly handled by the previous except clauses.

4.ZeroDivisionError: Raised when division or modulo by zero is encountered.

5.ValueError: Raised when a function receives an argument of correct type but improper value.

6.TypeError: Raised when an operation or function is applied to an object of an inappropriate type.

7.FileNotFoundError: Raised when a file or directory is requested but cannot be found.

8.IndexError: Raised when a sequence index is out of range.

9.KeyError: Raised when a dictionary key is not found.

10.NameError: Raised when a local or global name is not found.

11.AssertionError: Raised when an assert statement fails.
"""