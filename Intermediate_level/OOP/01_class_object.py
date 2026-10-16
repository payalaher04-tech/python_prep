# OOP class and objects

# a program to create one student object and print the student's details.
class Student:
    def __init__(self, name, age, city):   #defined initializer with the parameters
        self.name = name  #stored objects
        self.age = age
        self.city = city


student = Student("Payal", 22, "pune")  #recalling the class object with values

print("Name:", student.name) 
print("Age:", student.age)
print("City:", student.city)