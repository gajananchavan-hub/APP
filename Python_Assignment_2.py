def report_card(func):
    def wrapper(*args, **kwargs):
        print("----- Report Card -----")
        func(*args, **kwargs)
        print("-----------------------")
    return wrapper



class Report :
    college = "XYZ College"
    
    #constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    # class method
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college
    #magic method
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, College: {self.college}"
    #Decorator applied to display the report card
    
    @report_card
    def display_report(self):
       print(f"college: {Report.college}")
       print(self)
       if self.marks >= 40:
           print("Status: Pass")
       else:
           print("Status: Fail")
# main program 
student1 = Report("Alice", 101, 85)
student1.display_report()
print()  
#change college name using class method
Report.change_college("ABC University")
student2 = Report("Bob", 102, 35)
student2.display_report()
    
