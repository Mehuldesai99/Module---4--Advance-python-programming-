#>>> 5.Write a Python program to read last n lines of a file.

def read_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            return last_n_lines
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
file_name = 'myfile.txt' 
n = 5  # Number of lines to read

last_n_lines = read_last_n_lines(file_name, n)
if isinstance(last_n_lines, list):
    print(f"Last {n} lines of '{file_name}':")
    for line in last_n_lines:
        print(line.strip())
else:
    print(last_n_lines)