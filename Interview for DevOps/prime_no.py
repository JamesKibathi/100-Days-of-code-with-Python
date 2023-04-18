def prime(param):
    for i in range(2,param):
        if((param%i)==0):
            print(param,"is not prime number")
            break
    else:
        print(param,"is a prime number") 
            
num =int(print("Please enter the number:")) 

if num > 1:
    prime(num)
else:
    print("Enter a valid number")    