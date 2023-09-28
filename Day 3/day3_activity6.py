def calculate_area(length: float, width: float) -> float:
    area = length * width

    return area


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

print(f"The area of the rectangle is {calculate_area(length, width)}")
