# OOP: Polymorphism

# A program where the same method gives different results for different objects.

class Bike:
    def vehicle_sound(self):
        print("Bike makes a vroom sound")


class Car:
    def vehicle_sound(self):
        print("Car makes a horn sound")


bike = Bike()  # Created a Bike object
car = Car()    # Created a Car object

bike.vehicle_sound()  # Called method for the bike
car.vehicle_sound()   # Called method for the car