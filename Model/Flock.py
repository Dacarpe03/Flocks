from .Bird import Bird
import random


class Flock:
    def __init__(self, numberOfBirds, maxX, maxY):
        self.birds = []
        self.numberOfBirds = numberOfBirds

        self.maxX = maxX
        self.maxY = maxY

        for i in range(0, self.numberOfBirds):
            position = [random.randint(0, maxX-1), random.randint(0,maxY-1)]
            vector = [0.5, 0.5]
            self.birds.appen(Bird(id, position, vector))
