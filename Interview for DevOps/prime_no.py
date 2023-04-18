def prime_check(param):
    for i in range(2,param):
        if((param%i)==0):
            print(param,"is not prime number")
            break
    else:
        print(param,"is a prime number") 
            
num=int(input("Please enter the number:\n")) 

if num > 1:
    prime_check(num)
else:
    print("Enter a valid number!")    