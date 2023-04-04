"""
- Accepts user input of goal and dealine
print back:
- How much time remains until that deadline

"""
from datetime import datetime
user_input = input("Please enter goal and dealine\n")

input_filter= user_input.split(":")

print(input_filter)

input_dictionary = {"task":input_filter[0],"due_date":input_filter[1]}

print(input_dictionary)

goal =  input_dictionary["task"]

print(goal)

due_date = input_dictionary["due_date"]

valid_due_date = datetime.strptime(due_date,"%Y.%m.%d")

print(f"Valid due date is {valid_due_date}")

print (due_date)

today = datetime.today().strftime("%Y.%m.%d")

valid_today = datetime.strptime(today,"%Y.%m.%d")

print(f"Valid today is {valid_today}")

remaining_days = valid_due_date - valid_today

print(f"Dear user, you have {remaining_days.days} days to {goal}")



