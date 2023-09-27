
def summation(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + summation(n - 1)


print(summation(10))