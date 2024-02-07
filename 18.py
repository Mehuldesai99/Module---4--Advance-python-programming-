# >>> 18.What happens when „1‟== 1 is executed?

"""
when you execute the expression "1" == 1, you're comparing a string "1" to an integer 1 using the equality operator (==).

The result of this comparison will be False.

This is because in Python, the == operator compares the values of the operands. In this case, even though both "1" and 1 may represent the same numerical value, they are different types: one is a string, and the other is an integer. Python considers them to be different because they are different types, so the equality comparison results in False.

If you want to check whether a string represents a numerical value equal to an integer, you'd need to convert one of the values to the other's type before comparing them

string_value = "1"
integer_value = 1

# Convert string to integer and compare
if int(string_value) == integer_value:
    print("The values are equal.")
else:
    print("The values are not equal.")

"""