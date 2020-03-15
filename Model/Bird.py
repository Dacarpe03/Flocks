import numpy as np

class Bird:

    def __init__(self, id, position, vector):
        self.position = position
        self.vector = vector
        self.id = id

    def move(self):
        self.position[0] += self.vector[0]
        self.position[1] += self.vector[1]

    def goTo(self, x, y):
        print("Cambio destino")
        vx = x-self.position[0]
        vy = y-self.positon[0]
        newVector = [vx, vy]
        norm = np.linalg.norm(newVector)
        self.vector = newVector/norm
        print(self.vector)
