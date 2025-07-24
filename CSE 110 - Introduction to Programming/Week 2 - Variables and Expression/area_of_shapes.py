import math

square_length = float(input("What is the length of a side of the square? "))
print(f"The area of the square is: {square_length ** 2}")

rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {area:.1f}")

radius = float(input("What is the radius of the circle? "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area:.2f}")
