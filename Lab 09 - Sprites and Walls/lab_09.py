""" Sprite Sample Program """

import arcade
import random
import os

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GEM = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "THE CAVE OF WONDERS"

NUMBER_OF_GEMS = 50

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.physics_engine = None

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Says that cameras are going to exist
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        # Background Color
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Resets score
        self.score = 0

        # Creates player
        self.player_sprite = arcade.Sprite("female_adventurer_fall.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        #  --- Walls (Crates)

        # Random box
        wall = arcade.Sprite("box_crate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # Another random box
        wall = arcade.Sprite("box_crate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # And another random box
        wall = arcade.Sprite("box_crate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 136
        self.wall_list.append(wall)

        # --- Places some crates in a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite("box_crate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        # --- Places some crates into a loop
            coordinate_list = [[400, 500],
                               [470, 500],
                               [400, 570],
                               [470, 570]]

        # --- Loops coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("box_crate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for i in range(NUMBER_OF_GEMS):

            gem = arcade.Sprite("gem_blue.png", SPRITE_SCALING_GEM)

            gem_placed_successfully = False

            while not gem_placed_successfully:

                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)

                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)


                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)


                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:

                    gem_placed_successfully = True

            self.gem_list.append(gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()

        # Scrolled camera
        self.camera_for_sprites.use()

        # Draws sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        # Unscrolled camera
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def update(self, delta_time):
        self.physics_engine.update()

        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.gem_list.update()

        # Generate a list of all sprites that collided with the player.
        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.gem_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()