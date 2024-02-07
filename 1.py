#>>> 1. What is File function in python? What is keywords to create and write file.

"""
In Python, the open() function is used to create or open a file. It is commonly used in conjunction with the with statement, which ensures that the file is properly closed after its suite finishes, even if an exception is raised.

To create and write to a file in Python, you can use the open() function with the mode 'w' or 'a'. Here's a brief explanation of these modes:

'w' mode: Opens a file for writing. If the file already exists, it will truncate (i.e., erase its contents). If the file does not exist, it will be created.
'a' mode: Opens a file for writing but appends the new data at the end of the file, without truncating the existing content. If the file doesn't exist, it will be created.

ex:-
# Creating and writing to a file
with open('example.txt', 'w') as file:
    file.write('This is an example sentence.\n')
    file.write('This is another line in the file.')


"""