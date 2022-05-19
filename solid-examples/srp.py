""" 
Single Responsibility Principle (SRP)
Every software component(class, method, module...) should have one and only one responsibility.
Every software component(class, method, module...) should have one and only one reason the change.

"""


# Dont do it
"""
Reason the Changes:
1- Changes in Employee attributes
2- Changes database 
"""

class Employee:
    def __init__(self, salary: float):
        self.salary = salary

    def get_salary(self) -> float:
        pass

    def save(self, employee):
        print("Saved to postgre DB")
        #print("Saved to Mongo DB")

employee = Employee(1200)
employee.save(employee)

""" 
if we change database to postgre to mongo, 
we have change save method in Employee class, this changes violate SRP. 
"""



# Do it

class NewEmployee:
    def __init__(self, salary: float):
        self.salary = salary


class NewEmployeeDbManager:
    def save(self, employe: NewEmployee):
        print("Saved to Mongo DB")

new_employee = NewEmployee(1200)
new_employee_db_manager = NewEmployeeDbManager()
new_employee_db_manager.save(new_employee)

""" 
Now if i want to change database to postgre to mongo, 
just i need to change save method in NewEmployeeDbManager 
so i dont need change Employee class anymore.
"""