# Abstraction

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def maxSpeed(self):
        pass
    
myCar = Car() # Abstract sınıftan Object oluşturulmaz.

class Tesla(Car):
    def maxSpeed(self):
        print("200 km")

tesla= Tesla()
tesla.maxSpeed()


class Mercedes(Car):
    
    def maxSpeed(self):
        print("280 km")
        
mercedes= Mercedes()
mercedes.maxSpeed()

#Special Method


class Fruit():
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories
        
    def __str__(self):
        return f"{self.name}: {self.calories} calories"
     
    def __len__(self):
        return self.calories
    
Myfruit = Fruit(" Banana", 150)
Myfruit.calories
Myfruit.name
Myfruit.calories
print(Myfruit)



