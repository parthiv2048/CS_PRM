# TASK 1.1

students = []
while True:
    students_left = input("Are there any more students left? (Y/N): ")
    if students_left == "N":
        break
    name = input("What is your name?: ")
    email = input("What is your email address?: ")
    student_details = name + "#" + email
    students.append(student_details)

print("Student name" + " " * 20 + "Email Address")
for student_details in students:
    student_name = student_details[:student_details.index("#")]
    student_email = student_details[student_details.index("#")+1:]
    print(student_name + " " * (32-len(student_name)) + student_email)

# TASK 1.2

print("Student name" + " " * 20 + "Email Address")
for student_details in students:
    if student_details != None or len(student_details) != 0:
        student_name = student_details[:student_details.index("#")]
        student_email = student_details[student_details.index("#")+1:]
        print(student_name + " " * (32-len(student_name)) + student_email)

# TASK 1.3

query_name = input("What is your name?: ")
for student_details in students:
    student_name = student_details[:student_details.index("#")]
    if student_name == query_name:
        student_email = student_details[student_details.index("#")+1:]
        print("Email Address: " + student_email)

# TASK 1.4

query_name = input("What is your name (part or whole)?: ")
print("Student name" + " " * 20 + "Email Address")
for student_details in students:
    student_name = student_details[:student_details.index("#")]
    if query_name in student_name:
        student_email = student_details[student_details.index("#")+1:]
        print(student_name + " " * (32-len(student_name)) + student_email)

# TASK 1.6

# TASK 1.1 with TASK 1.6
students = []
while True:
    students_left = input("Are there any more students left? (Y/N): ")
    if students_left == "N":
        break
    name = input("What is your name?: ")
    email = input("What is your email address?: ")
    date = input("What is your date of birth? (DD/MM/YY): ")
    id = input("What is your student ID?: ")
    student_details = [name, email, date, id]
    students.append(student_details)

print("Student Name" + " " * 20 + "Email Address" + " " * 20 + "Date of birth" + " " * 20 + "Student ID")
for student_details in students:
    print(student_details[0] + " " * (32-len(student_details[0])), end="")
    print(student_details[1] + " " * (33-len(student_details[1])), end="")
    print(student_details[2] + " " * (33-len(student_details[2])), end="")
    print(student_details[3])

# TASK 1.2 with TASK 1.6

print("Student Name" + " " * 20 + "Email Address" + " " * 20 + "Date of birth" + " " * 20 + "Student ID")
for student_details in students:
    if student_details != None or len(student_details) != 0:
        print(student_details[0] + " " * (32-len(student_details[0])), end="")
        print(student_details[1] + " " * (33-len(student_details[1])), end="")
        print(student_details[2] + " " * (33-len(student_details[2])), end="")
        print(student_details[3])

# TASK 1.3 with TASK 1.6

query_name = input("What is your name?: ")
print("Student Name" + " " * 20 + "Email Address" + " " * 20 + "Date of birth" + " " * 20 + "Student ID")
for student_details in students:
    student_name = student_details[0]
    if query_name == student_name:
        student_email = student_details[1]
        print(student_name + " " * (32-len(student_name)) + student_email)

# TASK 1.4 with TASK 1.6

query_name = input("What is your name (part or whole)?: ")
print("Student Name" + " " * 20 + "Email Address" + " " * 20 + "Date of birth" + " " * 20 + "Student ID")
for student_details in students:
    student_name = student_details[0]
    if query_name in student_name:
        print(student_details[0] + " " * (32-len(student_details[0])), end="")
        print(student_details[1] + " " * (33-len(student_details[1])), end="")
        print(student_details[2] + " " * (33-len(student_details[2])), end="")
        print(student_details[3])
