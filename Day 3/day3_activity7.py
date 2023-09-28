def calculate(num1: float | int, num2: float | int, operator: str) -> float | int:
    """
    Calculates num1 and num2 based on the given operator. Returns float or int.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "//":
        return num1 // num2
    elif operator == "**":
        return num1**num2
    elif operator == "%":
        return num1 % num2


print(calculate(2, 3, "+"))
print(calculate(4, 5, "-"))
print(calculate(6, 7, "*"))
print(calculate(8, 9, "/"))
print(calculate(10, 11, "//"))
print(calculate(12, 13, "**"))
print(calculate(14, 15, "%"))
