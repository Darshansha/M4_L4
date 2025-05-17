try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an error!")
except SyntaxError:
    print("Separate numbers with a comma, like this: '1, 2'")
except:
    print("Wrong input")
else:
    print("There are no exceptions")
finally:
    print("This will execute no matter what")