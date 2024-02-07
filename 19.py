#>>> 19.How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

try:
    result = 10 / 2  
except ZeroDivisionError as e:
    # Handle the specific exception
    print("Error:", e)
else:
    # Execute if no exceptions occurred in the try block
    print("Result:", result)
finally:
    # This block is always executed
    print("Finally block executed")