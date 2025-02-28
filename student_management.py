class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}, Average Grade: {self.average_grade():.2f}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(name, student_id)
            print(f"Student {name} added.")

    def add_grade(self, student_id, grade):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
        else:
            self.students[student_id].add_grade(grade)
            print(f"Grade {grade} added to student ID {student_id}.")

    def display_students(self):
        for student in self.students.values():
            print(student)

    def find_student(self, student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
        else:
            print(self.students[student_id])


def main():
    system = StudentManagementSystem()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Display Students")
        print("4. Find Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            system.add_student(name, student_id)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            grade = float(input("Enter grade: "))
            system.add_grade(student_id, grade)
        elif choice == '3':
            system.display_students()
        elif choice == '4':
            student_id = input("Enter student ID: ")
            system.find_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
