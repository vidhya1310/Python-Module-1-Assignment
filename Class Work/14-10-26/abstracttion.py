from abc import ABC, abstractmethod

class Employee(ABC): # Abstract class

    def salary(self):
        pass

class ved(Employee):

    def salary(self):
        return 50000

class Hello(Employee):
    def salary(self):
        return 35000

class Hello1(Employee):
    def salary(self):
        return 10000

obj = ved()
print(obj.salary())
obj1 = Hello()
print(obj1.salary())
obj2 = Hello1()
print(obj2.salary())