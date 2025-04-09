# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 08:13:46 2025

@author: sam77
"""

class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
        
    def Circumferance(self):
        return 2*3.14*self.r
    def Area(self):
        return 3.14*self.r*self.r
    
#creating object
a_circle=Circle(2.0,2.0,1.0)
b_circle=Circle(3.0,3.0,2.0)

#accesing data and methods
print("Radius of a ",a_circle.r)
print("Area of a is ",a_circle.Area())  
print("Circumferance of a ",a_circle.Circumferance())
print("Radius of b ",b_circle.r)   

#for B
print("Radius of b is ",b_circle.r)
print("Area of b is ",b_circle.Area())
print("Circumferance of b ",b_circle.Circumferance())


#encapsulation: hiding data
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def get_radius(self):
        return self.r
    def set_redius(self,r):
        if r>0:
            self.r=r
        else:
            print("invalid radius")

c2=Circle(1,1,3)
print(c2.get_radius())
c2.set_redius(10)
print(c2.get_radius())




#inheritance

#base class
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    
    def area(self):
        return 3.14*self.r*self.r
    
    def circumferance(self):
        return 2*3.14*self.r
    
    def display_info(self):
        print(f"Center:({self.x},{self.y}),Radius:{self.r}")
        print(f"Area: {self.area()}:.2f")
        print(f"Circumferance:{self.circumferance():.2f}")

#derived class
class ColoredCircle(Circle):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, r) #call parent constructor
        self.color=color
        
        #overriding the display_info method
    def display_info(self):
        super().display_info()
        print(f"Color:{self.color}")
        
c1=ColoredCircle(0,0,5,"red")
c1.display_info()
        


#polymorphism

class Circle:
    def area(self):
        return "Calculating area of Circle"
class Square:
    def area(self):
        return "Calculating area of Square"

shapes=[Circle(),Square()]
for shape in shapes:
    print(shape.area())
    
#################3
#3 to 5
#7 april 2025

class Person:
    def __init__(self,name,age): #constructor
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"HEllo, my name is {self.name} and I am {self.age} years old")
                       
person1=Person("Alice",25) #object here, instance of class
person1.greet()

"""
encapsulation
hiding internal data and exposing only necessary parts
"""
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #private attribute
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance
    
ba1=BankAccount(300)
print(ba1.get_balance())
ba1.deposit(100)
#direct avoided
print(ba1.get_balance())


###################################


class Animal:
    def speak(self):
        print()
        
class Dog (Animal):
    def speak(self):
        print("bark")
d=Dog()
d.speak()



##############################3
#Polymorphism

class Cat:
    def speak(self):
        print("meow")
animals=[Dog(),Cat()]
for animal in animals:
    animal.speak()



##Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
#usage
circle1=Circle(5)
print("Area of Circle:",circle1.area())

































