student_grades = {}

while True:
    print("\n--- Student Grades List ---")
    print("1. Add New Student and Grade")
    print("2. Update Existing Student Grade")
    print("3. Print All Student Grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        if name in student_grades:
            print("Student already exists.")
        else:
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print("Student not found.")

    elif choice == '3':
        if not student_grades:
            print("No student records found.")
        else:
            print("\n--- All Student Grades ---")
            for student, grade in student_grades.items():
                print(f"{student}: {grade}")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select 1-4.")
