 # series = 0,1,1,2,3,5,8,13,21,34 [index 9]
n1=0
n2=1
temp_value = 0
last_index = int(input("Enter the Last index of your series\n"))

print(n1)
print(n2)
for i in range(0,last_index):
    temp_value = n1+n2
    n1 = n2
    n2 = temp_value
    print(f"Fibonacci series:",temp_value)





