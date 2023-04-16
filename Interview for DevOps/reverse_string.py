def reverse_string(my_string):
    temp_reverse = ""
    for i in my_string:
        print(i)
        temp_reverse = i + temp_reverse
    return temp_reverse 

my_string = "Test"   
reversed = reverse_string(my_string)   
print(reversed) 
