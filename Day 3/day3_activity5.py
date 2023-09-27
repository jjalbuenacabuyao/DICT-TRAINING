
def summation(num: int | float) -> int | float:
    sum = 0
    for i in range(num + 1):
        sum += i

    return sum


def factorial(num: int | float) -> int | float:
    factorial = 1
    for i in range(num + 1):
        factorial *= i

    return factorial


print(summation(10))
print(summation(5))
