# Student Record Mini Project

students = [
    {"name": "Priya", "age": 17, "marks": 89},
    {"name": "Gayatri", "age": 18, "marks": 87},
    {"name": "Bhavesh", "age": 19, "marks": 86},
    {"name": "John", "age": 18, "marks": 83},
    {"name": "Siya", "age": 19, "marks": 88},
    {"name": "Rani", "age": 17, "marks": 89}
]

while True:
    print("\n---- Student Record Menu ----")
    print("1. View all students")
    print("2. Show age 18 students")
    print("3. Search student by name")
    print("4. Calculate average marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1. View all students
    if choice == "1":
        for student in students:
            print(student)

    # 2. Show age 18 students
    elif choice == "2":
        for student in students:
            if student["age"] == 18:
                print(student)

    # 3. Search student by name
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for student in students:
            if student["name"] == search_name:
                print(student)
                found = True

        if not found:
            print("Student Not Found")

    # 4. Calculate average marks
    elif choice == "4":
        total = 0
        for student in students:
            total += student["marks"]

        average = total / len(students)
        print("Average Marks:", average)

    # 5. Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")



