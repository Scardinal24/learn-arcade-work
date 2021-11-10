""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10

class BeachBall:
    def __init__(self, position_x, position_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.radius = radius
        self.color = color

    def draw(self):

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class SandCastle:
    def __init__(self, position_x, position_y, radius, change_x, change_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        # Sand Castle
        x = self.position_x
        y = self.position_y
        arcade.draw_rectangle_filled(x, y, 20, 60, arcade.csscolor.BURLYWOOD)
        arcade.draw_rectangle_filled(x+35, y-10, 50, 40, arcade.csscolor.BURLYWOOD, 0)
        arcade.draw_rectangle_filled(x+55, y, 20, 60, arcade.csscolor.BURLYWOOD)
        arcade.draw_arc_filled(x+27, y-30, 20, 40, arcade.csscolor.PERU, 0, 180)
        arcade.draw_triangle_filled(x, y+50, x-20, y+20, x+20, y+20, arcade.csscolor.BURLYWOOD)
        arcade.draw_triangle_filled(x+75, y+20, x+35, y+20, x+55, y+50, arcade.csscolor.BURLYWOOD)

    def update(self):
        # Move sandcastle
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):


    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        # Load the sound when the game starts
        self.laser_sound = arcade.load_sound("laser.wav")
        self.error_sound = arcade.load_sound("error2.wav")

        self.set_mouse_visible(False)

        # creating the ball
        self.beach_ball = BeachBall(50, 50, 15, arcade.color.RUBY_RED)

        self.sand_castle = SandCastle(50, 50, 0, 0, 0, 15)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)
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

# Beach Ball
        self.beach_ball.draw()

# Sand Castle
        self.sand_castle.draw()

    def update(self, delta_time):
        self.sand_castle.update()

    def on_mouse_motion(self, x, y, dx, dy):

        self.beach_ball.position_x = x
        self.beach_ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.sand_castle.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.sand_castle.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.sand_castle.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.sand_castle.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.sand_castle.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.sand_castle.change_y = 0


def main():
    window = MyGame(640, 480, "Lab 7")
    arcade.run()


main()