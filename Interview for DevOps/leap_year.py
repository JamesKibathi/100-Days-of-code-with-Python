def check_year(year):
    if year%4 ==0:
        print("Leap Year")
    elif year%100 ==0 and year%400 ==0:
        print("Leap Year")
    else:
        print("Not Leap")

my_year =int(input("Enter your year\n"))
result= check_year(my_year)
print(result)