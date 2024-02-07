#>>> 11. Write a Python program to write a list to a file.

file_='myfile.txt' 

def write_list_to_file(file_, items):
    try:
        with open(file_, 'w') as file:
            for item in items:
                file.write(str(item) + '\n')  
        print(f"List has been written to '{file_}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

my_list = ['apple', 'banana', 'orange', 'grape']

file_path = 'output_list.txt' 

write_list_to_file(file_path, my_list)