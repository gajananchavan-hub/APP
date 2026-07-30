from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_role(self):
        pass


# Student Class (Inheritance)
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.__roll_no = roll_no      # Encapsulation
        self.__books = []

    def issue_book(self, book):
        self.__books.append(book)

    def get_books(self):
        return self.__books

    def show_role(self):
        print("Role: Student")

    def display(self):
        print(f"Name      : {self.name}")
        print(f"Roll No   : {self.__roll_no}")
        print(f"Books     : {self.__books}")


# Teacher Class (Inheritance)
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_role(self):
        print("Role: Teacher")

    def display(self):
        print(f"Name      : {self.name}")
        print(f"Subject   : {self.subject}")


# Main Program
s1 = Student("Gajanan", 101)
t1 = Teacher("Sharma", "Python")

# Encapsulation
s1.issue_book("Python Programming")
s1.issue_book("Data Structures")

# Runtime Polymorphism
people = [s1, t1]

for person in people:
    person.show_role()      # Different implementation for each class
    person.display()
    print("-" * 30)

# Getter Method
print("Books issued to student:", s1.get_books())
