import turtle as tl

class Sky:
    name = "Turtle"
    turtle = tl.Turtle()

    def __init__(self):
        self.name = "Sky"
        self.turtle = tl.Turtle()
        self.turtle.screen.bgcolor("orange")

    def pintar(self):
        self.turtle.color('red', 'yellow')
        self.turtle.begin_fill()
        while True:
            self.turtle.forward(200)
            self.turtle.left(170)
            if abs(self.turtle.pos()) < 1:
                break
        self.turtle.end_fill()

    def drawTriangle(self, x, y):
        tl.shape("triangle")
        tl.done()
