                                      #CLASSES
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def get_attributes(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}"

class Student(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age, id_number)
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_attributes(self):
        base = super().get_attributes()
        return f"{base}, Grades: {self.grades}"
    
class Teacher(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age, id_number)
        self.courses_teaching = []

    def assign_course(self, course_name):
        self.courses_teaching.append(course_name)

    def get_attributes(self):
        base = super().get_attributes()
        return f"{base}, Courses Teaching: {self.courses_teaching}"

class Course:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.students_IDs = []

    def add_student(self, student_id):
        if student_id not in self.students_IDs:
            self.students_IDs.append(student_id)

    def average_grade(self, students):
        total = 0
        count = 0
        for student_id in self.students_IDs:
            student = students.get(student_id)
            if student and self.name in student.grades:
                total += student.grades[self.name]
                count += 1
        if count == 0:
            return 0.0
        else:
            return total / count
        
    def get_attributes(self, students):
        info = f"Course Name: {self.name}\nTeacher ID: {self.teacher_id}\nStudents:\n"
        for student_id in self.students_IDs:
            student = students.get(student_id)
            if student:
                info += f" - {student.name} (ID: {student.id_number})\n"
        return info
    

                                      #FUNCTIONS
def add_student(name, age, id_number, students):
    students[id_number] = Student(name, age, id_number)

def add_teacher(name, age, id_number, teachers):
    teachers[id_number] = Teacher(name, age, id_number)

def create_course(course_name, teacher_id, teachers, courses):
    if teacher_id in teachers:
        teachers[teacher_id].assign_course(course_name)
        course = Course(course_name, teacher_id)
        courses.append(course)

def enroll_student(course_name, student_id, students, courses):
    for course in courses:
        if course.name == course_name:
            course.add_student(student_id)

def add_grade(student_id, course_name, grade, students):
    if student_id in students:
        students[student_id].add_grade(course_name, grade)

def print_gpa(student_id, students):
    student = students.get(student_id)
    if student:
        print(f"{student.name}'s GPA: {student.calculate_gpa():.2f}")

def print_course_average(course_name, courses, students):
    for course in courses:
        if course.name == course_name:
            avg = course.average_grade(students)
            print(f"Average grade in {course.name}: {avg:.2f}")