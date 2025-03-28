class Employee:
    def __init__(self,name,age,possition,salary):
        self.name= name
        self.age = age
        self.possition = possition
        self.salary = salary
    
    def increase_salary(self,percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} old . Employee is a {self.
                possition} with salary of ${self.salary}"
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, "
            f"{repr(self.age)}, "
            f"{repr(self.possition)}, "
            f"{repr(self.salary)})"
        )
    def __add__(self,other_employee):
        return Employee("New",self.age + other_employee.age, "dev",2000)

e = Employee("Kris",38,"dev",1200)
print(e)
print(repr(e))
print(eval(repr(e)))
e.increase_salary(5)
print( e + e)