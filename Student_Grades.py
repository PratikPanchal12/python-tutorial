# Student Grades Program

# Initial dictionary
students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        if name in students:
            print(f"{name} already exists with grade {students[name]}.")
        else:
            students[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} not found.")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
