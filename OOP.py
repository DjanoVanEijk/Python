from classes import Car
car_1 = Car("Toyota", "Camry", 2020, "Red")
car_2 = Car("Honda", "Civic", 2019, "Blue")
print(car_1.make) 
print(car_2.model) 

car_1.drive()
car_2.stop()

from classes import Dog, Cat
dog = Dog()
cat = Cat()
print(dog.alive)
print(cat.alive)    
dog.bark()
cat.meow()