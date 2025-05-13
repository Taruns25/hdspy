'''
creating a class called person
use init if you want to pass a value to it 
self is used to point to that argument youre passing
this is an example for encapsualtion
'''
'''
class person:
    def __init__(self,name,age,salary): 
        self.name=name # type: ignore
        self.age=age
        self.__salary=salary
    def show(self):
        return f"{self.name} is {self.age} years old and draws {self.__salary}"

p1=person("jon",23,100000)
print(p1.show())
print(p1.__salary)
'''

'''
inheritence , 
'''
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print (f"{self.name} is {self.age} years old")
    
class Employee(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary
        
    def show(self):
        super().show()
        print(f"and earns {self.salary}")

e1=Employee("jack",23,450000)
e1.show()
'''
'''
class Vehicle:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    
    def info(self):
        print(f"{self.model} manufactured in {self.year}")
        
class Car(Vehicle):
    def __init__(self, model, year,fuel_type):
        super().__init__(model, year)
        self.fuel_type=fuel_type
    
    def info(self):
        super().info()
        print(f"and uses {self.fuel_type}")
        
class ElectricCar(Car):
    def __init__(self,model,year,fuel_type,battery_range):
        super().__init__(model,year,fuel_type)
        self.battery_range=battery_range
        
    def info(self):
        super().info()
        print(f" has a range of {self.battery_range}")
    
v = Vehicle("Honda", 2015)
v.info()  

c = Car("Toyota", 2018, "Petrol")
c.info() 

e = ElectricCar("Tesla", 2022, "Electric", 500)
e.info()
'''
'''
method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

c = Calculator()
print(c.add(5))        # 5
print(c.add(5, 3))     # 8
print(c.add(5, 3, 2))  # 10
'''

from abc import ABC , abstractmethod
'''abstraction
class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class dog(Animal):
    def makeSound(self):
        return "woof woof hooman!"
    
d=dog()


print(d.makeSound())

    '''
    
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self,amount,card_number):
        self.amount=amount
        self.card_number=card_number
        
    def pay(self):
        return f"Paid ₹{self.amount} using Credit Card ending with {self.card_number}"

class UPIPayment(PaymentMethod):
    def __init__(self,amount,upi_id):
        self.upi_id=upi_id
        self.amount=amount
    def pay(self):
        return f"Paid ₹{self.amount} via UPI ID {self.upi_id}"

c=CreditCardPayment(1200,6789)
u=UPIPayment(900,"2tarun@upi")
print(c.pay( ))
print(u.pay())