class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        # add more parameters here
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 1250
        print("{PatientName}’s estimated insurance costs is {estimatedcost} dollars.".format(PatientName=self.name, estimatedcost=estimated_cost))
    
    def update_age(self, new_age):
        try:
            if isinstance(new_age, int):
                self.age = new_age
                print("{PatientName} is now {PatientAge} years old.".format(PatientName = self.name, PatientAge = self.age))
            else:
                raise ValueError
        except:
            print("Please enter a whole number")
        self.estimated_insurance_cost()
    
    def update_num_children(self, new_num_children):
        try:
            while type(new_num_children) == int:
                
                self.num_of_children = new_num_children
                if self.num_of_children > 1:
                    print("{PatientName} has {PatientNumberofChildren} children.".format(PatientName = self.name, PatientNumberofChildren = self.num_of_children))
                else:
                    print("{PatientName} has {PatientNumberofChildren} child.".format(PatientName = self.name, PatientNumberofChildren = self.num_of_children))
        except ValueError:
            print("Please enter a whole number")
        self.estimated_insurance_cost()
  
    def patient_profile(self):
        patient_info = {}
        patient_info["Name"] = self.name
        patient_info["Age"] = self.age
        patient_info["Sex"] = self.sex
        patient_info["Number of Children"] = self.num_of_children
        patient_info["Smoker"] = self.smoker
        return patient_info

    def update_bmi(self, new_bmi):
        self.bmi = new_bmi
        print("{PatientName} now has a BMI of {PatientBMI}".format(PatientName = self.name, PatientBMI = self.bmi))
        self.estimated_insurance_cost()



patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

patient1.estimated_insurance_cost()
patient1.update_age(25)
patient1.update_num_children(2.1)
patient1.update_bmi(24)
print(patient1.patient_profile())