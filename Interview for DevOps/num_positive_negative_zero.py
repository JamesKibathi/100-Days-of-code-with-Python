def num_check(num):
    if num ==0:
        print("Number is zero or invalid")
    elif num > 0:
        print("It's a positive number")
    else:
        print("Negative number")

num_input = float(input("Please enter a number\n"))
result = num_check(num_input)
print(result)