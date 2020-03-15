import arcade
from Model.Flock import Flock

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000

N_BIRDS = 1
RADIUS_BIRD = 5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.flock = Flock(N_BIRDS, SCREEN_WIDTH, SCREEN_HEIGHT)

    #CONTROLS
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.flock.redirect(x, y)

    #INIT
    def setup(self):
        # Set up your game here
        arcade.set_background_color(arcade.color.AMAZON)
        pass

    #DRAWING
    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        for bird in self.flock.birds:
            self.drawBird(bird)

    def drawBird(self, bird):
        x = bird.currentPosition[0]
        y = bird.currentPosition[1]
        arcade.draw_circle_filled(x, y, RADIUS_BIRD, arcade.color.YELLOW)

    #STEP
    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.flock.move()

def main():
    v1 = [10,5]
    v2 = [20,3]
    print(v1+v2)
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()



if __name__ == "__main__":
    main()