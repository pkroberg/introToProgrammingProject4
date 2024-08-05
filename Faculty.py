from CollegeEmployee import CollegeEmployee

class Faculty(CollegeEmployee):
    def __init__(self):
        super().__init__()
        self.is_tenured = False

    def set_data(self):
        super().set_data()
        tenured = input("Is the faculty member tenured? (yes/no): ").strip().lower()
        self.is_tenured = tenured == 'yes'

    def display(self):
        super().display()
        print(f"Tenured: {'Yes' if self.is_tenured else 'No'}")