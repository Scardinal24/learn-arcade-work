"""
Testing how to draw stuff.
"""
import arcade

# Open a window
arcade.open_window(600,600,"Drawing Example")

arcade.set_background_color(arcade.csscolor.BLUE_VIOLET)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,599,300,0, arcade.csscolor.POWDER_BLUE)

arcade.finish_render()

arcade.run()