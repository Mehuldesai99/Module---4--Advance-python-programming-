#>>> 9.Write a Python program to count the number of lines in a text file.


file = 'myfile.txt'  

def count_lines(file):
    try:
        with open(file, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return -1   

num_lines = count_lines(file)

if num_lines != -1:
    print(f"The file '{file}' has {num_lines} lines.")