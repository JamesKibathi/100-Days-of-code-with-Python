
def calculate_average(lst):
    return sum(lst)/len(lst)

#Prompt user to enter a list
user_input = input("Create a comma separated list\n")

#convert input string to a list
to_list = user_input.split(",")

print(f"This is the list: {to_list}")
print(f"The length is: {len(to_list)}")

# Convert list elements into numbers
for i in range(len(to_list)):
    to_list[i]=int(to_list[i])

# print("Sum",sum(to_list))
avg = calculate_average(to_list)
print(f"The average is: {avg}")




