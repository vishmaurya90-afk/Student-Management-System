students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
