'''

Project 4

Main Program - implements a list of four “regular” CollegeEmployee, three Faculty, and seven Students. 

Programmer: Oberg, Parker

Course: CSC1019-FBN

'''

# imports
from Person import Person
from CollegeEmployee import CollegeEmployee
from Faculty import Faculty
from Student import Student


class CollegeList:
    def __init__(self):
        self.college_employees = []
        self.faculty = []
        self.students = []

    def add_person(self, person_type):
        if person_type == 'C':
            if len(self.college_employees) < 4:
                ce = CollegeEmployee()
                ce.set_data()
                self.college_employees.append(ce)
            else:
                print("Error: Cannot add more than 4 College Employees.")
        elif person_type == 'F':
            if len(self.faculty) < 3:
                f = Faculty()
                f.set_data()
                self.faculty.append(f)
            else:
                print("Error: Cannot add more than 3 Faculty members.")
        elif person_type == 'S':
            if len(self.students) < 7:
                s = Student()
                s.set_data()
                self.students.append(s)
            else:
                print("Error: Cannot add more than 7 Students.")
        else:
            print("Invalid person type.")

    def display_report(self):
        print("\nCollege Employees:")
        if not self.college_employees:
            print("No College Employees entered.")
        else:
            for ce in self.college_employees:
                ce.display()

        print("\nFaculty:")
        if not self.faculty:
            print("No Faculty entered.")
        else:
            for f in self.faculty:
                f.display()

        print("\nStudents:")
        if not self.students:
            print("No Students entered.")
        else:
            for s in self.students:
                s.display()

def main():
    college_list = CollegeList()
    while True:
        person_type = input("Enter person type (C for CollegeEmployee, F for Faculty, S for Student, Q to quit): ").strip().upper()
        if person_type == 'Q':
            break
        college_list.add_person(person_type)

    college_list.display_report()

if __name__ == "__main__":
    main()
