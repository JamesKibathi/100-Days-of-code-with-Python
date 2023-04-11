class Student:
    def __init__(self,fname,lname,email,course):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.course = course  

    def display_credentials(self):
        print(f"My name is {self.first_name} {self.last_name}, currently enrolled at {self.course}. Email me at {self.email}")  

student1 = Student("James", "Njenga", "fake@email.com","Software Engineering")       
student1.display_credentials()
