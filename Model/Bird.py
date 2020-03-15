
class Bird:

    def __init__(self, position, vector):
        self.position = position
        self.vector = vector

    def move(self):
        self.position[0] += self.vector[0]
        self.position[1] += self.vector[1]