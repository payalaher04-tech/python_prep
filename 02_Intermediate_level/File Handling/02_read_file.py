# File handling - reading from a file

file = open("student.txt", "r")  # opened the file in read mode

content = file.read()  # read the complete file content

print("Student Information:")
print(content)

file.close()  # closed the file


