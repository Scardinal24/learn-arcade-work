"""
Made by Sammy Cardinal.

This is a program of a drawing or Lab 02 in Intro to Programming.
This uses the Python programming and the Arcade Library.

"""

# Importing from the "arcade" library
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_sand():
    # Setting the sand
    arcade.draw_lrtb_rectangle_filled(0, 800, 250, 0, arcade.color.APRICOT)

# Drawing the Sun
def draw_sun():
    """ Draw the sun """
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

    # Rays to the left, right, up, and down
    arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

    # Diagonal rays
    arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

def draw_cloud(x, y):
    # Cloud 1
    arcade.draw_circle_filled(200 + x - 200, 450 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(240 + x - 200, 460 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(210 + x - 200, 480 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(170 + x - 200, 480 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)


def draw_cloud_two(x, y):
    # Cloud 2
    arcade.draw_circle_filled(750 + x - 700, 450 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(710 + x - 700, 460 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(680 + x - 700, 480 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_circle_filled(720 + x - 700, 480 + y - 450, 30, arcade.csscolor.FLORAL_WHITE)

def draw_sandcastle():
    # Sand Castle
    arcade.draw_rectangle_filled(400, 260, 20, 60, arcade.csscolor.BURLYWOOD)
    arcade.draw_rectangle_filled(435, 250, 50, 40, arcade.csscolor.BURLYWOOD, 0)
    arcade.draw_rectangle_filled(455, 260, 20, 60, arcade.csscolor.BURLYWOOD)
    arcade.draw_arc_filled(427, 230, 20, 40, arcade.csscolor.PERU, 0, 180)
    arcade.draw_triangle_filled(400, 310, 380, 280, 420, 280, arcade.csscolor.BURLYWOOD)
    arcade.draw_triangle_filled(475, 280, 435, 280, 455, 310, arcade.csscolor.BURLYWOOD)

def draw_palmtrees():
    # Palm trees
    arcade.draw_rectangle_filled(80, 200, 25, 300, arcade.csscolor.SIENNA)
    arcade.draw_rectangle_filled(270, 270, 25, 300, arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(120, 350, 80, 40, arcade.csscolor.DARK_GREEN, 0, 180)
    arcade.draw_arc_filled(115, 370, 80, 40, arcade.csscolor.DARK_GREEN, 0, 180, 35)
    arcade.draw_arc_filled(65, 370, 80, 40, arcade.csscolor.DARK_GREEN, 180, 360, 125)
    arcade.draw_arc_filled(300, 440, 80, 40, arcade.csscolor.DARK_GREEN, 0, 180, 35)
    arcade.draw_arc_filled(250, 440, 80, 40, arcade.csscolor.DARK_GREEN, 180, 360, 125)
    arcade.draw_arc_filled(50, 350, 80, 40, arcade.csscolor.DARK_GREEN, 0, 180)
    arcade.draw_arc_filled(310, 415, 80, 40, arcade.csscolor.DARK_GREEN, 0, 180)
    arcade.draw_arc_filled(240, 415, 80, 40, arcade.csscolor.DARK_GREEN, 0, 180)
    arcade.draw_circle_filled(265, 425, 15, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(280, 425, 15, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(270, 410, 15, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(76, 360, 15, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(90, 360, 15, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(80, 345, 15, arcade.csscolor.SADDLE_BROWN)

def draw_hammock(x, y):
    # Hammock
    arcade.draw_arc_filled(170 + x - 170, 250 + y - 250, 190, 60, arcade.csscolor.SLATE_BLUE, 180, 360, 15)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_sand()
    draw_sun()
    draw_cloud(200, 450)
    draw_cloud_two(700, 450)
    draw_sandcastle()
    draw_palmtrees()
    draw_hammock(170, 250)

    # Finish and run
    arcade.finish_render()
    arcade.run()

main()