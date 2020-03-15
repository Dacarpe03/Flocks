import arcade
from Model.Bird import Bird

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.bird = Bird([0, 0], [0.5, 0.5])
        self.radiusBird = 5
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.drawBird(self.bird)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.bird.move()
        pass

    def drawBird(self, bird):
        x = bird.position[0]
        y = bird.position[1]
        arcade.draw_circle_filled(x, y, self.radiusBird, arcade.color.YELLOW)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()



if __name__ == "__main__":
    main()