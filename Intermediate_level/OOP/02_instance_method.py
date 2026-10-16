# OOP instance method

# a program to create a student object and display its details using a method.
class Student:
    def __init__(self, name, age, city):   # defined initializer with the required parameters
        self.name = name      # stored name inside the object
        self.age = age 
        self.city = city# stored age inside the object

    def display(self):        # defined a method to display student details
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


student = Student("Payal", 22, "Pune")  # created a student object with values

student.display()         # called the display method using the object