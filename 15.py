# >>>15. When will the else part of try-except-else be executed?

"""
In a try-except-else block in Python, the else block is executed only if no exceptions occur in the preceding try block. If any exception is raised within the try block, the flow of execution jumps to the appropriate except block, and the else block is skipped.

try:
    # Code where exceptions might occur
    # ...
except SomeException:
    # Handle specific exceptions
    # ...
else:
    # Execute if no exceptions occurred in the try block
    # ...

The else block is typically used to contain code that should run only if the code in the try block executes without any exceptions. It's useful for separating the normal code flow from the error-handling code.

    

"""