'''
	 Hospital Patient Management System					
						
	Develop a Python application to maintain patient records.					
						
	Requirements					
	Create a Patient class with:					
		Patient ID				
		Name				
		Treatment Cost				
	Categorize patients as:					
		General				
		Special				
	Create a Hospital class.					
	Add patients.					
	Display all records.'''					
  
  
  class Patient:
    def __init__(self, patient_id, name, treatment_cost, category):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category

    def display(self):
        print(f"Patient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print(f"Cost       : {self.treatment_cost}")
        print(f"Category   : {self.category}")
        print("-" * 30)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        for patient in self.patients:
            patient.display()


hospital = Hospital()

n = int(input("Enter number of patients: "))

for i in range(n):
    pid = int(input("Enter Patient ID: "))
    name = input("Enter Name: ")
    cost = float(input("Enter Treatment Cost: "))
    category = input("Enter Category (General/Special): ")
    hospital.add_patient(Patient(pid, name, cost, category))

print("\nPatient Records")
hospital.display_patients()
