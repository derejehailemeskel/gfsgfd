import math

def circle_area(radius):
    return math.pi * radius ** 2

# Input radius
radius = float(input("Enter the radius of the circle: "))

# Call the function
area = circle_area(radius)

print(f"The area of the circle with radius {radius} is: {area}")

