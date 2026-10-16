# OOP class variable and instance variable

# a program to show the difference between class and instance variables.
class Student:
    college = "Samarth College"  #common value shared by all student objects

    def __init__(self, name):
        self.name = name    #each object gets its own name


student1 = Student("Payal")     #created first student object
student2 = Student("Sakshi")   # created second student object
student3 = Student("Suhani") 

print(student1.name, student1.college)
print(student2.name, student2.college)
print(student3.name, student3.college)