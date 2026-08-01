''' 								
 Student Management System								
								
Develop a Python application to manage student details using Object-Oriented Programming.								
								
Requirements								
Create a Student class with the following data members:								
	Roll Number							
	Name							
	Marks							
Assign Grade based on marks:								
	A (Marks ≥ 90)							
	B (Marks ≥ 75)							
	C (Marks ≥ 60)							
	F (Marks < 60)							
Create a College class.								
Add student objects to the college.								
Display all student details. '''			

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade()}")
        print("-" * 30)


class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            student.display()


college = College()

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    college.add_student(Student(roll, name, marks))

print("\nStudent Details")
college.display_students()
