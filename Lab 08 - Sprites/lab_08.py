import random
import arcade

# --- Sound effects ---
error_sound = arcade.load_sound("error2.wav")
coin_sound = arcade.load_sound("coin2.wav")

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_SLIME = 0.2
SPRITE_SCALING_BAD_SLIME = 0.2
SLIME_COUNT = 100
BAD_SLIME_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# how the
class Slime(arcade.Sprite):

    """
    This is the class that represents the good slime that needs to be collected
    """

    def reset_pos(self):
        # Reset the slime to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the slime
        self.center_y -= 1

        # See if the slime has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class BadSlime(arcade.Sprite):

    def reset_pos(self):
        # Reset the slime to a random spot above the screen
        self.center_y = random.randrange(- 100, - 20)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the slime
        self.center_y += 1

        # See if the slime has fallen off the bottom of the screen.
        # If so, reset it.
        if self.bottom > 600:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Slimetacular Adventure")

        # Variables that will hold sprite lists.
        self.player_list = None
        self.slime_list = None
        self.bad_slime_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BROWN)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.slime_list = arcade.SpriteList()
        self.bad_slime_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from Python Arcade Library
        self.player_sprite = arcade.Sprite("slimePurple.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(SLIME_COUNT):
            # Create the slime instance
            # Coin image from Python Arcade Library
            slime = Slime("slimeBlue.png", SPRITE_SCALING_SLIME)

            # Position the coin
            slime.center_x = random.randrange(SCREEN_WIDTH)
            slime.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.slime_list.append(slime)

        for i in range(BAD_SLIME_COUNT):
            # Create the slime instance
            # Coin image from Python Arcade Library
            bad_slime = BadSlime("slimeGreen.png", SPRITE_SCALING_BAD_SLIME)

            # Position the coin
            bad_slime.center_x = random.randrange(SCREEN_WIDTH)
            bad_slime.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.bad_slime_list.append(bad_slime)

    def on_draw(self):
        arcade.start_render()

        self.bad_slime_list.draw()
        self.slime_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.slime_list == 0:
            arcade.draw_text("GAME OVER",
                             150, 230,
                             arcade.color.BLACK, 24)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.slime_list.update()
        self.bad_slime_list.update()

        # Generate a list of all sprites that collided with the player.
        slimes_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                  self.slime_list)

        bad_slimes_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                   self.bad_slime_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for slime in slimes_hit_list:
            slime.remove_from_sprite_lists()
            self.score += 1

            arcade.play_sound(coin_sound)

        for bad_slime in bad_slimes_hit_list:
            bad_slime.remove_from_sprite_lists()
            self.score -= 1

            arcade.play_sound(error_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()