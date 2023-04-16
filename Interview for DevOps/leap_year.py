def check_year(year):
    if year%4 ==0 and (year%100 !=0)|(year%400 ==0):
       return("Leap Year")
    else :
      return("Not Leap Year")
  
my_year =int(input("Enter your year\n"))
result= check_year(my_year)
print(result)