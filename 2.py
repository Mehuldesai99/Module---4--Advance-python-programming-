#>>> 2.Write a Python program to read an entire text file.


# print("start")
# try:
#     file_name = 'myfile.txt'
#     open(file_name, 'x')
#     a= 40
#     print(a)
# except FileExistsError:
#     print(f"ERROR, {file_name} file already exist")
# except Exception as e:
#     print(f"ERROR, {e}")
# print("end")

# file = 'myfile.txt'

# f = open(file, 'w')
# # f.write("This is a python code")
# lines = ['this is a line 1\n', 'this is a line 2\n', 'this is a line 3\n', 'this is a line 4\n', 'this is a line 5\n', 'this is a line 6\n', 'this is a line 7\n', 'this is a line 8\n', 'this is a line 9\n', 'this is a line 10']
# f.writelines(lines)
# f.close()


try:
    file_name = 'myfile.txt'  

    # Open the file in read mode
    file = open(file_name, 'r')
    content = file.read()   
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found")