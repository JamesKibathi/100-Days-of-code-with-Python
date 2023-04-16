# Formula => n(n+1)/2
def sum_of_natural_numbers(param):
    return(param*(param+1)/2)

num = float(input("Enter a number\n"))
if num > 0:
    print("The sum of N natural numbers is:",sum_of_natural_numbers(num))  
else:
    print("Please enter a valid number")      
