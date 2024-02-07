#>>> 4.Write a Python program to read first n lines of a file.


file='myfile.txt'
n=5

def read_first_n_lines(file, n):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
            for i in range(min(n, len(lines))):
                print(lines[i].rstrip())
    except FileNotFoundError:
        print("File not found.")

read_first_n_lines(file, n)