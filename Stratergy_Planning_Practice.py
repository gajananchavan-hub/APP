#Employee Management System 

# ---------- Employee Class ----------
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("-------------------------")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      :", self.salary)


# ---------- Employee List ----------
employees = []


# ---------- Add Employee ----------
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, department, salary)
        employees.append(emp)

        print("Employee Added Successfully!")

    except ValueError:
        print("Invalid Input! Please enter correct values.")


# ---------- Display Employees ----------
def display_employees():
    if len(employees) == 0:
        print("No Employee Records Found.")
    else:
        for emp in employees:
            emp.display()


# ---------- Search Employee ----------
def search_employee():
    search_id = int(input("Enter Employee ID to Search: "))

    for emp in employees:
        if emp.emp_id == search_id:
            emp.display()
            return

    print("Employee Not Found.")


# ---------- Update Salary ----------
def update_salary():
    search_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.emp_id == search_id:
            emp.salary = float(input("Enter New Salary: "))
            print("Salary Updated Successfully!")
            return

    print("Employee Not Found.")


# ---------- Delete Employee ----------
def delete_employee():
    search_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.emp_id == search_id:
            employees.remove(emp)
            print("Employee Deleted Successfully!")
            return

    print("Employee Not Found.")


# ---------- Main Menu ----------
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
