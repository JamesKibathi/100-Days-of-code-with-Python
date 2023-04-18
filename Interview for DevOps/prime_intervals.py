def prime_checker(First, Second):
    for i in range(First, Second+1):
        for j in range(2,i):
            if((i%j)==0):
                print(i,"is a prime")
                break
            else:
                print(i,"is a prime number")
                
FirstInterval = int(input("Please enter the first interval:\n"))
SecondInterval = int(input("Please enter the second interval:\n"))

if((FirstInterval > 1 and SecondInterval) and FirstInterval < SecondInterval):
    prime_checker(FirstInterval,SecondInterval)
else:
    print("Enter a valid range!")