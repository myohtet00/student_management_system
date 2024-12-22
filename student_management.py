import csv
import os

# Define the path to the CSV file
CSV_FILE = 'data/students.csv'

# Define the Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = int(grade)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Function to load students from the CSV file
def load_students():
    students = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(Student(row['Name'], row['Age'], row['Grade']))
    return students

# Function to save students to the CSV file
def save_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Grade'])
        writer.writeheader()
        for student in students:
            writer.writerow({'Name': student.name, 'Age': student.age, 'Grade': student.grade})

# Function to add a new student
def add_student(students):
    name = input("Enter student's name: ")
    while True:
        try:
            age = int(input("Enter student's age: "))
            break
        except ValueError:
            print("Invalid input. Age must be an integer.")
    while True:
        try:
            grade = int(input("Enter student's grade: "))
            break
        except ValueError:
            print("Invalid input. Grade must be a number.")
    students.append(Student(name, age, grade))
    save_students(students)
    print("Student added successfully!")

# Function to view all students
def view_students(students):
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

# Function to update a student's grade
def update_grade(students):
    name = input("Enter the name of the student whose grade you want to update: ")
    for student in students:
        if student.name == name:
            while True:
                try:
                    new_grade = int(input(f"Enter new grade for {student.name}: "))
                    student.grade = new_grade
                    save_students(students)
                    print("Grade updated successfully!")
                    return
                except ValueError:
                    print("Invalid input. Grade must be a number.")
    print("Student not found.")

# Function to delete a student
def delete_student(students):
    name = input("Enter the name of the student you want to delete: ")
    for student in students:
        if student.name == name:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

# Main menu-driven interface
def main():
    students = load_students()
    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Update a student's grade")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_grade(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()