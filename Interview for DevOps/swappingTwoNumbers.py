# Swapping without a temporary variable

# num1 =input("Enter the first number\n") 
# num2 =input("Enter the second number\n") 

num1 =20
num2 = 80

if num1 < num2:

    print("Before swap:",num1,num2)

    num2 = num2 + num1 #num2 =30
    num1 = num2 - num1 #num1 = 20
    num2 = num2 - num1 #num2 = 10

    print("After swap:",num1,num2)
else:
    print("Before swap",num1,num2)

    num1 = num1+num2 
    num2 = num1-num2 
    num1 = num1-num2 

    print("After swap",num1,num2)