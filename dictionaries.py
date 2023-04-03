

def days_to_units(days,conversion_unit):
    if conversion_unit == "hours":
       return f" {days} days are  {days * 24} hours"
    elif conversion_unit == "minutes":
        return f" {days} days are  {days * 24*60} minutes"
    else:
        print("Unsupported unit")


def validate_and_execute():
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,days_and_units_dictionary["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0,please enter a valid positive number")
        else:
            print("You entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user,enter a number of days and conversion units!\n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_units_dictionary)
    validate_and_execute()
