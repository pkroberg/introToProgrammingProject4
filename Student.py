from Person import Person

class Student(Person):
    def __init__(self):
        super().__init__()
        self.major = ""
        self.gpa = 0.0

    def set_data(self):
        super().set_data()
        self.major = input("Enter major: ")
        self.gpa = float(input("Enter GPA: "))

    def display(self):
        super().display()
        print(f"Major: {self.major}, GPA: {self.gpa}")