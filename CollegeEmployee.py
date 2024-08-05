'''

Project 4

CollegeEmployee Class for CollegeList

Programmer: Oberg, Parker

Course: CSC1019-FBN

'''

from Person import Person

class CollegeEmployee(Person):
    def __init__(self):
        super().__init__()
        self.social_security_number = ""
        self.annual_salary = 0.0
        self.department_name = ""

    def set_data(self):
        super().set_data()
        self.social_security_number = input("Enter social security number: ")
        self.annual_salary = float(input("Enter annual salary: "))
        self.department_name = input("Enter department name: ")

    def display(self):
        super().display()
        print(f"SSN: {self.social_security_number}, Salary: {self.annual_salary}, Department: {self.department_name}")