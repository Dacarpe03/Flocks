import arcade
from Model.Flock import Flock

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000

N_BIRDS = 20
RADIUS_BIRD = 5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.flock = Flock(N_BIRDS, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here

        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        for bird in self.flock.birds:
            self.drawBird(bird)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        for bird in self.flock.birds:
            bird.move()
        pass

    def drawBird(self, bird):
        x = bird.position[0]
        y = bird.position[1]
        arcade.draw_circle_filled(x, y, RADIUS_BIRD, arcade.color.YELLOW)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()



if __name__ == "__main__":
    main()