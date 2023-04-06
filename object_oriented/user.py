class User:
    # constructor function - class is like an object constructor
    def __init__(self, email, name, password, current_job_title):
        self.name = name
        self.email = email
        self.password = password
        self.current_job_title = current_job_title

    # Methods - functions that belong to a class
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User: {self.name}, currently works as a {self.current_job_title}. You can contact them at {self.email}")


# Creating an object - instance of a class
"""
user_james = User("njenga@gmail.com", "James Njenga", "pwd1", "Software Engineer")
user_james.get_user_info()
user_james.change_job_title("Tech Lead")
user_james.get_user_info()

user_two = User("info@novasavannah.com", "Nova Savannah", "super secret", "CTO and Co-founder")
user_two.get_user_info()
"""