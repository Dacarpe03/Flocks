import turtle as tl

class Window:

    def __init__(self):

    def __pintar__(self):
        tl.color('red', 'yellow')
        tl.begin_fill()
        while True:
            tl.forward(200)
            tl.left(170)
            if abs(tl.pos()) < 1:
                break
        tl.end_fill()
        tl.done()

