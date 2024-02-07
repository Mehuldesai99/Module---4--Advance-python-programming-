#>>> 6.Write a Python program to read a file line by line and store it into a list

file_name = 'myfile.txt' 

try:
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(f"Lines from '{file_name}':")
        for line in lines:
            print(line)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")