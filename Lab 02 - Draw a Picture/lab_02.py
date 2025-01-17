"""
Made by Sammy Cardinal.

This is a program of a drawing or Lab 02 in Intro to Programming.
This uses the Python programming and the Arcade Library.

"""

# Importing from the "arcade" library
import arcade

# Opening the window and using the necessary functions
arcade.open_window(800, 600, "Drawing Example")

# Background color (Sky)
arcade.set_background_color(arcade.color.SKY_BLUE)

# Drawing ready command
arcade.start_render()

# Drawing (Beach/Sand)
arcade.draw_lrtb_rectangle_filled(0, 800, 250, 0, arcade.color.APRICOT)

# Sun
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

# Cloud 1
arcade.draw_circle_filled(200, 450, 30, arcade.csscolor.FLORAL_WHITE)
arcade.draw_circle_filled(240, 460, 30, arcade.csscolor.FLORAL_WHITE)
arcade.draw_circle_filled(210, 480, 30, arcade.csscolor.FLORAL_WHITE)
arcade.draw_circle_filled(170, 480, 30, arcade.csscolor.FLORAL_WHITE)

# Cloud 2
arcade.draw_circle_filled(750, 450, 30, arcade.csscolor.FLORAL_WHITE)
arcade.draw_circle_filled(710, 460, 30, arcade.csscolor.FLORAL_WHITE)
arcade.draw_circle_filled(680, 480, 30, arcade.csscolor.FLORAL_WHITE)
arcade.draw_circle_filled(720, 480, 30, arcade.csscolor.FLORAL_WHITE)

# Sand Castle
arcade.draw_rectangle_filled(400, 260, 20, 60, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(435, 250, 50, 40, arcade.csscolor.BURLYWOOD, 0)
arcade.draw_rectangle_filled(455, 260, 20, 60, arcade.csscolor.BURLYWOOD)
arcade.draw_arc_filled(427, 230, 20, 40, arcade.csscolor.PERU, 0, 180)
arcade.draw_triangle_filled(400, 310, 380, 280, 420, 280, arcade.csscolor.BURLYWOOD)
arcade.draw_triangle_filled(475, 280, 435, 280, 455, 310, arcade.csscolor.BURLYWOOD)

# Hammock with two trees

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

# Hammock
arcade.draw_arc_filled(170, 250, 190, 60, arcade.csscolor.SLATE_BLUE, 180, 360, 15)

# --- Finish Drawing ---
arcade.finish_render()

# Keeping the window up until closed
arcade.run()