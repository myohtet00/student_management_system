# Student Management System

This is a simple Student Management System implemented in Python. It allows you to add, view, update, and delete student records stored in a CSV file.

## Project Structure

 student_management/
│
├── data/
│   └── students.csv
│
├── student_management.py
└── README.md

## Features

- Add a new student
- View all students
- Update a student's grade
- Delete a student

## Usage

1. Clone the repository or download the source code.
2. Ensure you have Python installed on your system.
3. Run the `student_management.py` script.

## Functions
    load_students()
        - Loads student records from the CSV file located at data/students.csv.

    save_students(students)
        - Saves the list of student records to the CSV file located at data/students.csv.

    main()
        - Main menu-driven interface to interact with the Student Management System.

# Student Class
The Student class represents a student with the following attributes:
    name: The name of the student.
    age: The age of the student.
    grade: The grade of the student.

# CSV File
The student records are stored in a CSV file located at data/students.csv. The CSV file has the following columns:
    Name
    Age
    Grade

# Example
Here is an example of how the CSV file might look:
    Name,Age,Grade
    John Doe,17,10
    Jane Smith,16,9
