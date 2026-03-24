class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The " + self.model + " is driving.")
        
    def stop(self):
        print("The " + self.model + " has stopped.")

class Animal:
   
   alive = True

   def eat(self):
        print("This animal is eating.")
   
   def sleep(self):
        print("This animal is sleeping.")

class Dog(Animal):

    def bark(self):
        print("Woof!")

class Cat(Animal):

    def meow(self):
        print("Meow!")