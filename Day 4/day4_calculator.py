import math


def add(x: int | float, y: int | float) -> int | float:
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    return x - y


def multiply(x: int | float, y: int | float) -> float:
    return x * y


def divide(x: int | float, y: int | float) -> float:
    return x / y


def modulo(x: int | float, y: int | float) -> int:
    return x % y


def exponent(x: int | float, y: int | float) -> int | float:
    return x**y


def floor_division(x: int | float, y: int | float) -> int:
    return x // y


def factorial(x: int | float) -> int | float:
    return math.factorial(x)


def summation(x: list[int | float]) -> int | float:
    return sum(x)


def area(length: int | float, width: int | float) -> int | float:
    return length * width


def radius(circumference: int | float) -> int | float:
    return circumference / (2 * math.pi)


def circumference(radius: int | float) -> int | float:
    return 2 * math.pi * radius


def square_root(num: int | float) -> int | float:
    return math.sqrt(num)


def volume(length: int | float, width: int | float, height: int | float) -> int | float:
    return length * width * height


def volume_of_cylinder(height: int | float) -> int | float:
    return (math.pi**2) * height


def area_of_circle(radius: int | float) -> int | float:
    return math.pi * radius


def speed(distance: int | float, time: int | float) -> int | float:
    return distance / time
