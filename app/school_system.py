from app.models import Course, Student
from app.storage import load_data, save_data


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id.lower() == course_id.lower():
                return course
        return None

    def add_student(self):
        print("\n--- Add Student ---")
        student_id = input("Student ID: ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        phone_number = input("Phone: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return
        if self.find_student_by_id(student_id):
            print("A student with this ID already exists.")
            return
        if not name:
            print("Student name cannot be empty.")
            return
        if "@" not in email:
            print("Email must contain @.")
            return
        if not phone_number:
            print("Phone number cannot be empty.")
            return

        self.students.append(Student(student_id, name, email, phone_number))
        print(f"{name} has been added successfully.")

    def view_students(self):
        print("\n--- Students ---")
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()
            print("-" * 30)

    def search_student(self):
        print("\n--- Search Student ---")
        search_term = input("Enter student ID or name: ").strip().lower()

        if not search_term:
            print("Search term cannot be empty.")
            return

        matches = []
        for student in self.students:
            same_id = student.student_id.lower() == search_term
            name_found = search_term in student.name.lower()
            if same_id or name_found:
                matches.append(student)

        if not matches:
            print("No matching student found.")
            return

        for student in matches:
            student.display()
            print("-" * 30)

    def add_course(self):
        print("\n--- Add Course ---")
        course_id = input("Course ID: ").strip()
        course_name = input("Course Name: ").strip()
        trainer_name = input("Trainer Name: ").strip()
        capacity_text = input("Capacity: ").strip()

        if not course_id:
            print("Course ID cannot be empty.")
            return
        if self.find_course_by_id(course_id):
            print("A course with this ID already exists.")
            return
        if not course_name:
            print("Course name cannot be empty.")
            return
        if not trainer_name:
            print("Trainer name cannot be empty.")
            return

        try:
            capacity = int(capacity_text)
        except ValueError:
            print("Course capacity must be a number.")
            return

        if capacity <= 0:
            print("Course capacity must be greater than 0.")
            return

        self.courses.append(Course(course_id, course_name, trainer_name, capacity))
        print(f"{course_name} has been added successfully.")

    def view_courses(self):
        print("\n--- Courses ---")
        if not self.courses:
            print("No courses found.")
            return

        for course in self.courses:
            enrolled = self.count_students_in_course(course.course_id)
            course.display()
            print(f"Registered: {enrolled}/{course.capacity}")
            print("-" * 30)

    def count_students_in_course(self, course_id):
        count = 0
        for registration in self.registrations:
            if registration["course_id"].lower() == course_id.lower():
                count += 1
        return count

    def register_student(self):
        print("\n--- Register Student to Course ---")
        student_id = input("Student ID: ").strip()
        course_id = input("Course ID: ").strip()

        student = self.find_student_by_id(student_id)
        if not student:
            print("Student not found.")
            return

        course = self.find_course_by_id(course_id)
        if not course:
            print("Course not found.")
            return

        for registration in self.registrations:
            same_student = registration["student_id"].lower() == student_id.lower()
            same_course = registration["course_id"].lower() == course_id.lower()
            if same_student and same_course:
                print(f"{student.name} is already registered for this course.")
                return

        if self.count_students_in_course(course_id) >= course.capacity:
            print("Registration failed. This course is already full.")
            return

        self.registrations.append(
            {"student_id": student.student_id, "course_id": course.course_id}
        )
        print(f"{student.name} successfully registered for {course.course_name}.")

    def view_students_in_course(self):
        print("\n--- Students in a Course ---")
        course_id = input("Course ID: ").strip()
        course = self.find_course_by_id(course_id)

        if not course:
            print("Course not found.")
            return

        students_in_course = []
        for registration in self.registrations:
            if registration["course_id"].lower() == course_id.lower():
                student = self.find_student_by_id(registration["student_id"])
                if student:
                    students_in_course.append(student)

        print(f"\nStudents registered for {course.course_name}:")
        if not students_in_course:
            print("No students registered for this course.")
            return

        for student in students_in_course:
            student.display()
            print("-" * 30)

    def view_courses_for_student(self):
        print("\n--- Courses for a Student ---")
        student_id = input("Student ID: ").strip()
        student = self.find_student_by_id(student_id)

        if not student:
            print("Student not found.")
            return

        registered_courses = []
        for registration in self.registrations:
            if registration["student_id"].lower() == student_id.lower():
                course = self.find_course_by_id(registration["course_id"])
                if course:
                    registered_courses.append(course)

        print(f"\nCourses registered by {student.name}:")
        if not registered_courses:
            print("This student has not registered for any courses.")
            return

        for course in registered_courses:
            course.display()
            print("-" * 30)

    def save_data(self):
        save_data(self.students, self.courses, self.registrations)
        print("Data saved successfully.")

    def load_data(self):
        self.students, self.courses, self.registrations = load_data()
        print("Data loaded successfully.")
