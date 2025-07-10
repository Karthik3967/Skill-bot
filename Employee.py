class Employee:
    def __init__(self, name=" ", salary=0.0, age=0):
        self.__name = name
        self.__salary =salary
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be greater than 0.")
    def get_salary(self):
        return self.__salary
    def set_age(self, age):
        if 18 <= age <= 100:
            return "Error: Age must be between 18 and 100."
        else:
            return self.__age

Employee=input("Employee name : ")
salary=int(input("Employee salary : "))
age=int(input("Employee age : "))
emp=Employee()
emp.setName(Employee)
emp.setmarks(salary)
emp.set_age(age)
print(emp.getname())
print(emp.getsalary())
print(emp.getage())