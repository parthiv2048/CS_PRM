# TASK 2.1

fh = open("students.txt", "w+")
print("Format for Student ID: 2 letters followed by 4 numbers")
while True:
    students_left = input("Are there anymore students left? (Y/N): ")
    if students_left == "N":
        break
    format_correct = False
    while not(format_correct):
        student_id = input("Enter Student ID: ")
        if student_id[:2].isalpha() and student_id[2:].isdigit():
            format_correct = True
        else:
            print("Wrong format")
            print("Format for Student ID: 2 letters followed by 4 numbers")
    student_email = input("Enter Student Email: ")
    student_details = student_id + "#" + student_email
    fh.write(student_details + "\n")
fh.close()

# TASK 2.2

fh = open("students.txt", "r")
query_id = input("Enter Student ID: ")
id_found = False
for line in fh.readlines():
    if line[:6] == query_id:
        print("Email Address: " + line[7:len(line)-1])
        id_found = True
        break
if not(id_found):
    print("ID not found")
fh.close()

# TASK 2.3

fh = open("students.txt", "r")
query_id = input("Enter Student ID (Part or Whole): ")
id_found = False
for line in fh.readlines():
    if query_id in line[:6]:
        print("Email Address: " + line[7:len(line)-1])
        id_found = True
if not(id_found):
    print("ID not found")
fh.close()

# TASK 2.4

fh = open("students.txt", "a")
while True:
    students_left = input("Are there anymore students left? (Y/N): ")
    if students_left == "N":
        break
    format_correct = False
    while not(format_correct):
        student_id = input("Enter Student ID: ")
        if student_id[:2].isalpha() and student_id[2:].isdigit():
            format_correct = True
        else:
            print("Wrong format")
            print("Format for Student ID: 2 letters followed by 4 numbers")
    student_email = input("Enter Student Email: ")
    student_details = student_id + "#" + student_email
    fh.write(student_details + "\n")
fh.close()

# TASK 2.6

# TASK 2.1 with TASK 2.6

fh = open("students.txt", "w+")
print("Format for Student ID: 2 letters followed by 4 numbers")
while True:
    students_left = input("Are there anymore students left? (Y/N): ")
    if students_left == "N":
        break
    format_correct = False
    while not(format_correct):
        student_id = input("Enter Student ID: ")
        if student_id[:2].isalpha() and student_id[2:].isdigit():
            format_correct = True
        else:
            print("Wrong format")
            print("Format for Student ID: 2 letters followed by 4 numbers")
    fh.write(student_id + "\n")
    student_email = input("Enter Student Email: ")
    fh.write(student_email + "\n")
    student_address = input("Enter Student Home Address: ")
    fh.write(student_address + "\n")
    student_tutor = input("Enter Student Tutor: ")
    fh.write(student_tutor + "\n")
fh.close()

# TASK 2.2 with TASK 2.6

fh = open("students.txt", "r")
query_id = input("Enter Student ID: ")
id_found = False
lines = fh.readlines()
for line in lines:
    if lines.index(line) % 4 == 0 and line[:6] == query_id:
        email_address = lines[lines.index(line) + 1]
        email_address = email_address[:len(email_address)-1]
        print("Email Address: " + email_address)
        id_found = True
        break
if not(id_found):
    print("ID not found")
fh.close()

# TASK 2.3 with TASK 2.6

fh = open("students.txt", "r")
query_id = input("Enter Student ID: ")
id_found = False
lines = fh.readlines()
for line in lines:
    if lines.index(line) % 4 == 0 and query_id in line[:6]:
        email_address = lines[lines.index(line) + 1]
        email_address = email_address[:len(email_address)-1]
        print("Email Address: " + email_address)
        id_found = True
if not(id_found):
    print("ID not found")
fh.close()

# TASK 2.4 with TASK 2.6

fh = open("students.txt", "a")
print("Format for Student ID: 2 letters followed by 4 numbers")
while True:
    students_left = input("Are there anymore students left? (Y/N): ")
    if students_left == "N":
        break
    format_correct = False
    while not(format_correct):
        student_id = input("Enter Student ID: ")
        if student_id[:2].isalpha() and student_id[2:].isdigit():
            format_correct = True
        else:
            print("Wrong format")
            print("Format for Student ID: 2 letters followed by 4 numbers")
    fh.write(student_id + "\n")
    student_email = input("Enter Student Email: ")
    fh.write(student_email + "\n")
    student_address = input("Enter Student Home Address: ")
    fh.write(student_address + "\n")
    student_tutor = input("Enter Student Tutor: ")
    fh.write(student_tutor + "\n")
fh.close()
