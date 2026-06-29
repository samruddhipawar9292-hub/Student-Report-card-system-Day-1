class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = {}

    def add_grade(self, subject, marks):
        self.grades[subject] = marks
        print(f"{subject} grade updated successfully!")

    def display_report_card(self):
        print("\n===== REPORT CARD =====")
        print(f"Name     : {self.name}")
        print(f"Roll No. : {self.roll_no}")

        total = 0

        print("\nSubjects and Marks:")
        for subject, marks in self.grades.items():
            print(f"{subject} : {marks}")
            total += marks

        if len(self.grades) > 0:
            average = total / len(self.grades)
            print(f"\nTotal Marks : {total}")
            print(f"Average     : {average:.2f}")

        print("========================")



student1 = Student("Kunal", 101)


student1.add_grade("Maths", 90)
student1.add_grade("Python", 95)
student1.add_grade("DBMS", 88)


student1.add_grade("Maths", 92)

student1.display_report_card()
