#inheritance
class Employee:
    def __init__(self,name ,email ,department, salary):
        self.name=name
        self.email=email
        self.department=department
        self.salary=salary

    def show_details(self):
        print(self.name, self.department,self.salary)

class PermanentEmployee(Employee):
    def __init__(self, name, email, department, salary,cover,increment):
        super(). __init__(name ,email ,department, salary)
        self.cover=cover
        self.increment=increment

class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary,tanure):
        super().__init__(name, email, department, salary)
        self.tanure=tanure
    def show_details(self):
        print(f"name {self.name}")
        print(f"email {self.email}")
        print(f"Contract length {self.tanure}")

p1=PermanentEmployee("Hellen Moi","Moi@gmail.com","Hr",150000,"Britam",2500)
c1=ContractEmployee("Julia","julia@com","Sales",45_000,5)

p1.show_details()
c1.show_details()




