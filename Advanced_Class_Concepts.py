from abc import ABC, abstractmethod

# Abstract Class
class Employee(ABC):
    company = "ABC Technologies"      # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary        # Encapsulation (Private Variable)

    # Property (Getter)
    @property
    def salary(self):
        return self.__salary

    # Property (Setter)
    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid Salary!")

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static Method
    @staticmethod
    def company_info():
        print("Employees work in an IT Company.")

    # Abstract Method
    @abstractmethod
    def work(self):
        pass


# First Parent Class
class Manager(Employee):

    def work(self):
        print(f"{self.name} manages the team.")

    # Operator Overloading
    def __add__(self, other):
        return self.salary + other.salary


# Second Parent Class
class Trainer:
    def train(self):
        print("Conducts employee training.")


# Multiple Inheritance
class TeamLead(Manager, Trainer):

    # Method Overriding
    def work(self):
        print(f"{self.name} leads the project team.")

    def display(self):
        print("\nEmployee Details")
        print("----------------")
        print("Name    :", self.name)
        print("Salary  :", self.salary)
        print("Company :", self.company)


# Main Program
emp1 = TeamLead("Gajanan", 50000)
emp2 = TeamLead("Rahul", 60000)

emp1.display()
emp1.work()
emp1.train()

Employee.company_info()

Employee.change_company("OpenAI Pvt Ltd")

print("\nAfter Company Change:")
emp2.display()

# Using Property Setter
emp1.salary = 55000
print("\nUpdated Salary:", emp1.salary)

# Operator Overloading
print("Total Salary =", emp1 + emp2)
