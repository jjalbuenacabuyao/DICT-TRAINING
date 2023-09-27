score = float(input("Enter a score: "))

letter_grade = ""
feedback = ""

if score >= 90 and score <= 100:
    letter_grade = "A"
    feedback = "Excellent"
elif score >= 80 and score <= 89:
    letter_grade = "B"
    feedback = "Good job"
elif score >= 70 and score <= 79:
    letter_grade = "C"
    feedback = "You're doing okay"
elif score >= 60 and score <= 69:
    letter_grade = "D"
    feedback = "You need to work harder"
elif score < 60:
    letter_grade = "F"
    feedback = "You didn't pass"

if score < 0 or score > 100:
    print("Invalid score.")
else:
    print(f"{score} - {letter_grade} {feedback}")
