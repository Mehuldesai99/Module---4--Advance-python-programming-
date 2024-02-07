#>>> 12. Write a Python program to copy the contents of a file to another file.

source_file_path = 'myfile.txt' 

def copy_file(source_file,new_file):
    try:
        with open(source_file, 'r') as source:
            with open(new_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' have been copied to '{new_file}' successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

new_file='copy_file.txt' 

copy_file(source_file_path,new_file)