print("Hello champ!")  # String

# String concatenation

print("There are " + str(1440) + " minutes in a day")
print(f"There are {24 * 60} minutes in a day")

# Variables

calculation_to_units = 24
name_of_units = "hours"
print(f"7 days are {7 * calculation_to_units} {name_of_units}")
print(f"30 days are {30 * calculation_to_units} {name_of_units}")


# Functions
def days_to_units():
    print("There are x days in a week")
    print("Function can have multiple lines")


days_to_units()


# Func parameters

def calculate_days_to_hours(days):
    return f"{days} days are {days * calculation_to_units} {name_of_units}"


calculate_days_to_hours(35)
calculate_days_to_hours(20)
calculate_days_to_hours(100)

# User input
user_input = input("Hey user please enter days so I can convert to hours\n")
input_to_integer = int(user_input)
calculated = calculate_days_to_hours(input_to_integer)
print(calculated)

# Conditionals
