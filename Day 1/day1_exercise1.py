gross_salary = float(input("Enter your Gross Salary: "))
deduction = float(input("Enter the amount of deduction: "))
fullname = input("Enter your full name: ").upper()

netpay = gross_salary - deduction

print(
    f"Hi Sir/Ma'am {fullname} based on the provided information your net pay is {netpay}"
)
