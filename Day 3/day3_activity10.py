student_records: list[tuple] = []


def add_student(name: str, age: int, grade: str) -> None:
    student_info = (name, age, grade)
    student_records.append(student_info)


def display_students() -> None:
    for record in student_records:
        print(
            f"Student Name: {record[0]}\nStudent Age: {record[1]}\nStudent Grade: {record[2]}"
        )
        print()


while True:
    print(
        """
Commands:
    1 - enter student info
    2 - display student info
    3 - exit
"""
    )
    # Using string to avoid error if a number was entered
    command = input("Enter command (1, 2 or 3): ")

    if command == "1":
        student_name = input("Enter student name: ").title()
        student_age = int(input("Enter student age: "))
        student_grade = input("Enter student grade: ").upper()

        add_student(student_name, student_age, student_grade)

    elif command == "2":
        display_students()

    elif command == "3":
        print("Loop terminated")
        break

    else:
        print("Invalid command")
