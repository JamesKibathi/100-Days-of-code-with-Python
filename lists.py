# Lists - used to store multiple items in a single variable
# - can contain different types

def days_to_units(days):
    return(f"There are {days*60} minutes in {days} days")

def validate_and_execute():
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0,please enter a valid positive number")
        else:
            print("You entered a negative number, no conversion for you")   
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")

user_input = ""
while user_input!= "exit":
    user_input = input("Hey user,enter a number of days and I will convert it to hours!\n")
    for num_of_days in user_input.split(","):
        validate_and_execute()


# List methods
months=["Jan","Feb","April","May"]
print(months[1])
months.append("June")
print(months)