'''

Project 4

Person Class for CollegeList

Programmer: Oberg, Parker

Course: CSC1019-FBN

'''

class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.street_address = ""
        self.zip_code = ""
        self.phone_number = ""

    def set_data(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.street_address = input("Enter street address: ")
        self.zip_code = input("Enter zip code: ")
        self.phone_number = input("Enter phone number: ")

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}, Address: {self.street_address}, Zip Code: {self.zip_code}, Phone Number: {self.phone_number}")