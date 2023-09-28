def divide(numerator: int | float, denominator: int | float) -> float | None:
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    else:
        return result
    

result = divide(10, 5)

print(result)
