 # Set - as with Lists,used to store multiple items but does NOT allow duplicate values
 # REPRESENTED using curly braces {10,2,5}

def convert_to_hours(days):
    return(f"There are {days*24} hours in {days} days")

def validate_and_execute():
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_value = convert_to_hours(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a zero,please enter a valid positive number")
        else:
            print("You entered a negative, no conversion for you")

    except ValueError:
        print("Your input is not a valid number!Don't ruin my program")


user_input = input("Hey User! Please enter days for conversion\n")  
my_set = set(user_input.split(","))
print(my_set)
for num_of_days in my_set:
     validate_and_execute()  

# Basic set operations
months={"Jan","Feb","March"}
#NB:Cannot access individual element using index - can only access in a loop
for element in months:
    print(element)

months.add("April")
print(months)  # Not displayed in any particular order
months.remove("Jan")
print(months)
