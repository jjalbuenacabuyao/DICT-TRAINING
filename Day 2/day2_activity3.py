name = input("Name: ")

math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))

average = (math + science + english) / 3
print(f"Average: {average}")

failed_subjects = ""

message = f"Congratulations, you have passed the semester. But you need to re-enroll"

PASSING_GRADE = 75

if math < PASSING_GRADE:
    failed_subjects += " math,"

if science < PASSING_GRADE:
    failed_subjects += " science,"

if english < PASSING_GRADE:
    failed_subjects += " english,"

if average < PASSING_GRADE:
    print("Sorry you failed the semester")
elif average >= PASSING_GRADE and failed_subjects == "":
    print("Congratulations, you have passed the semester")
else:
    print(f"{message}{failed_subjects} subject.")

