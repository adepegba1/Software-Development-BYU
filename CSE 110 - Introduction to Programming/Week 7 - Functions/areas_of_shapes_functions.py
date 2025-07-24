"""
Write functions to compute and return the areas of squares, rectangles, and circles. 
These functions should not display the values directly, but rather should return them, 
so they could be used in other parts of the program.

Write a function compute_area_square that accepts a single value as a parameter, 
and then computes the area and returns it.

Below the function, write code to prompt the user for the side of a square and save it into a variable,
then pass this variable to the function to compute the area. 
Finally, get the result back from the function and display it.

Repeat the previous step to write and test the functions compute_area_rectangle 
and compute_area_circle.

Write a loop to ask the user what kind of shape they have, 
then prompt for the length of a side, or sides, or radius, and 
then calls the appropriate function, and displays the result. 
The program should continue looping until the user enters "quit" for the shape.

Recognize that you can compute the area of a square by passing the task along to a function 
that computes the areas of rectangles, by giving it the side of the square twice.

Change your program so that the compute_area_square function doesn't compute the area directly, 
but instead calls the compute_area_rectangle to do the work. 
It should pass the square side length to it (twice) and 
then return the value that the compute_area_rectangle function computes.
"""
import math
def compute_area_square(side):
    area = pow(side, 2)
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = math.pi * pow(radius, 2)
    return area

user_input = input("""What shape would you like to find the area? Square, Rectangle or Circle: 
or type 'quit' to stop the program: """)

while user_input.lower() != 'quit':
    if user_input.lower() == 'square':
        side = float(input('What is the side of the square: '))
        area = compute_area_square(side)
        print(f"The area of the square is {area:.2f}")
    
    elif user_input.lower() == 'rectangle':
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        area = compute_area_rectangle(length, width)
        print(f"The area of a rectangle is {area:.2f}")

    elif user_input.lower() == 'circle':
        radius = float(input('What is the radius of the circle? '))
        area = compute_area_circle(radius)
        print(f"The area of the circle is {area:.2f}")
    else:
        print('Invalid shape, Try again')
    user_input = input("""What shape would you like to find the area? Square, Rectangle or Circle: 
or type 'quit' to stop the program: """)
