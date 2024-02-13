from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        bonus = self.base_salary * 0.2
        return self.base_salary + bonus


class Developer(Employee):
    def calculate_salary(self):
        bonus = self.base_salary * 0.1
        return self.base_salary + bonus


class Tester(Employee):
    def calculate_salary(self):
        bonus = self.base_salary * 0.3
        return self.base_salary + bonus


manager = Manager("John", 50000)
developer = Developer("Alice", 60000)
tester = Tester("Steven", 45000)

print(f"{manager.name}'s salary: ${manager.calculate_salary()}")
print(f"{developer.name}'s salary: ${developer.calculate_salary()}")
print(f"{tester.name}'s salary: ${tester.calculate_salary()}")
