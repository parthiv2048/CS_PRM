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

print("Student name          Email Address")
for student_details in students:
    print(student_details[:student_details.index("#")] + " " * (22-len(student_details[:student_details.index("#")])) + student_details[student_details.index("#")+1:])

# TASK 1.2

for student_details in students:
    if student_details != None:
        print(student_details[:student_details.index("#")] + " " * (22-len(student_details[:student_details.index("#")])) + student_details[student_details.index("#")+1:])

# TASK 1.3

query_name = input("What is your name?: ")
for student_details in students:
    student_name = student_details[:student_details.index("#")]
    if student_name == query_name:
        student_email = student_details[student_details.index("#")+1:]
        print("Email Address: " + student_email)

# TASK 1.4

query_name = input("What is your name (part or whole)?: ")
print("Student name          Email Address")
for student_details in students:
    student_name = student_details[:student_details.index("#")]
    if query_name in student_name:
        print(student_details[:student_details.index("#")] + " " * (22-len(student_details[:student_details.index("#")])) + student_details[student_details.index("#")+1:])

# TASK 1.6
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

print("Student Name          Email Address          Date of birth          Student ID")
for student_details in students:
    print(student_details[0] + " " * (22-len(student_details[0])), end="")
    print(student_details[1] + " " * (23-len(student_details[0])), end="")
    print(student_details[2] + " " * (23-len(student_details[0])), end="")
    print(student_details[3])
