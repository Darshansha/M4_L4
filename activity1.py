number = int(input("Enter a number: "))

try:
    print("The number is", number)
except ValueError as ex:
    print("Exception", ex)