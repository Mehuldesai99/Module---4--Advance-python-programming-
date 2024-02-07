# >>> 3. Write a Python program to append text to a file and display the text.

file_name = 'myfile.txt' 

try:
    # Append text to the file
    with open(file_name, 'a') as file:
        text_to_append = "\nThis text will be appended."
        file.write(text_to_append)
    
    # Display the appended text
    with open(file_name, 'r') as file:
        appended_content = file.read()
        print("Appended content:")
        print(appended_content)

except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")