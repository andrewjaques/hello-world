students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id }
    students.append(student)

student_list = get_students_titlecase()

keep_entering = "Y"

while keep_entering == "Y":
    enter_a_student = raw_input("Enter a new student? Type Y or N and hit return: ")
    if enter_a_student == "N":
        exit()
    else:
        student_name = raw_input("Enter student name: ")
        student_id = raw_input("Enter student ID: ")

add_student(student_name, student_id)

print_students_titlecase()
