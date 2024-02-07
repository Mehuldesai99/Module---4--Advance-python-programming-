#>>> 20.Write python program that user to enter only odd numbers, else will raise an exception.

def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 0:
                raise ValueError("Even number entered. Please enter an odd number.")
            else:
                return num
        except ValueError as e:
            print(e)

try:
    odd_number = get_odd_number()
    print("odd number entered:", odd_number)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")