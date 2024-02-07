#>>> 17.When is the finally block executed?

"""
The finally block lets you execute code, regardless of the result of the try- and except blocks.

1.No Exception: If no exceptions occur in the try block, the code in the finally block will be executed after the try block finishes executing.

try:
    # Code where exceptions might occur
    # ...
except SomeException:
    # Handle specific exceptions
    # ...
finally:
    # This block is always executed
    # ...

    
2.Exception Occurs and Handled: If an exception occurs within the try block and it's caught by an appropriate except block, the code in the finally block will still be executed after the except block.

try:
    # Code where exceptions might occur
    # ...
except SomeException:
    # Handle specific exceptions
    # ...
finally:
    # This block is always executed
    # ...

    
3.Exception Occurs and Not Handled: If an exception occurs in the try block and is not caught within the code (no matching except block), the finally block still gets executed before the exception propagates up the call stack.

try:
    # Code where exceptions might occur
    # ...
finally:
    # This block is always executed
    # ...

"""