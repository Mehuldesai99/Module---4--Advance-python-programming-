# >>> 7.Write a Python program to read a file line by line store it into a variable.

file = 'myfile.txt' 

# Open the file in read mode
with open(file, 'r') as file:
    empty_variable = ''
    
    for line in file:
        empty_variable += line

# Printing the content to show it's stored in the variable
print(empty_variable)