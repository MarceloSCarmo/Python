import math

list_of_shapes = ['Square', 'Circle', 'Rectangle']


def square(square_side):
    return int(square_side) ** 2

def rectangle(rectangle_length, rectangle_width):
    return int(rectangle_length) * int(rectangle_width)
 
def circle(circle_radius):
    return math.pi * (int(circle_radius) ** 2)

shape = ''

while shape != 'quit':
    #clean_data = list_of_shape.strip()
    #data = clean_data.split(',')

    #square_data = data[0]
    #circle_data = data[1]
    #rectangle_data = data[2]
    shape = input("What shape do you have? ")
    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = square(side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = rectangle(length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}")
            
    