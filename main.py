from classes_and_functions import (
    add_student, add_teacher, create_course,
    enroll_student, add_grade,
    print_gpa, print_course_average
)
import os


students = {}
teachers = {}
courses = []

add_teacher("Καθηγητής Παπαδόπουλος", 45, "T001", teachers)
add_student("Μαρία", 19, "S001", students)
add_student("Γιάννης", 20, "S002", students)

create_course("Math 101", "T001", teachers, courses)
enroll_student("Math 101", "S001", students, courses)
enroll_student("Math 101", "S002", students, courses)

add_grade("S001", "Math 101", 90, students)
add_grade("S002", "Math 101", 80, students)

print_gpa("S001", students)
print_course_average("Math 101", courses, students)


# Εμφάνιση working directory
print(f"Current working directory: {os.getcwd()}")

# Αποθήκευση σε αρχείο
with open("students_data.txt", "w", encoding="utf-8") as f:
    for student in students.values():
        f.write(student.get_attributes() + "\n")

with open("teachers_data.txt", "w", encoding="utf-8") as f:
    for teacher in teachers.values():
        f.write(teacher.get_attributes() + "\n")

with open("courses_data.txt", "w", encoding="utf-8") as f:
    for course in courses:
        f.write(course.get_attributes(students) + "\n")