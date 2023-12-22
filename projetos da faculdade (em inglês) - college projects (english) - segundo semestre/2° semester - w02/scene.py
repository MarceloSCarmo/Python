# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500


    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height)
    draw_snowman(canvas)
  



    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    
def draw_cloud(canvas, scene_width, scene_height):

    x = 100
    y = 300

    diameter = 15

    half_height = round(scene_height * 2)
    min_diam = 15
    max_diam = 90       

    for i in range(100):
        x = random.randint(50, scene_width - max_diam)
        y = random.randint(300, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, 
                outline="snow1", fill="snow1")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")
    
    tree_center_x = 1700
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
    
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
        tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
        trunk_left, trunk_top, trunk_right, bottom,
        outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
        skirt_right, trunk_top,
        skirt_left, trunk_top,
        outline="gray20", width=1, fill="dark green")
    
def draw_snowman(canvas):
    
    #   creating the body of the snowman
    x = 200
    y = 20

    diameter = 90

    draw_oval(canvas, x, y, x + diameter, diameter,
        outline="snow1", fill="snow1")
    
    #   creating the head of the snowman
    x = 215
    y = 140

    diameter = 65

    draw_oval(canvas, x, y, x + diameter, y - 50,
        outline="snow1", fill="snow1")

    #   creating the right eye of the snowman    
    x = 240
    y = 125

    diameter = 1

    draw_oval(canvas, x, y, x - 10, y - 10,
        outline="black", fill="black")
    
    #   creating the Left eye of the snowman
    x = 260
    y = 125

    diameter = 1

    draw_oval(canvas, x, y, x - 10, y - 10,
        outline="black", fill="black")

    #   creating the bottons of the snowman
    x = 250
    y = 70  # first botton

    diameter = 1

    draw_oval(canvas, x, y, x - 10, y - 10,
        outline="black", fill="black")
    
    x = 250
    y = 50  # second botton

    diameter = 1

    draw_oval(canvas, x, y, x - 10, y - 10,
        outline="black", fill="black")
    
    #   creating the nouse
    x = 255
    y = 115  

    diameter = 1

    draw_oval(canvas, x, y, x - 20, y - 10,
        outline="darkOrange2", fill="darkOrange2")
    
    #   creating the armies

    draw_line(canvas, x - 40, y - 35, 180, 50, width=5, fill="black")   # right
    draw_line(canvas, x + 18, y - 30, 305, 50, width=5, fill="black")   # left

# Call the main function so that
# this program will start executing.
main()