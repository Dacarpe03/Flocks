from .Bird import Bird
import random


class Flock:

    SPEED = 4

    CREATION_LIMIT = 100

    def __init__(self, numberOfBirds, maxX, maxY):
        self.birds = []
        self.numberOfBirds = numberOfBirds

        self.maxX = maxX
        self.maxY = maxY

        for i in range(0, self.numberOfBirds):
            position = [random.randint(self.CREATION_LIMIT, self.maxX-self.CREATION_LIMIT), random.randint(self.CREATION_LIMIT, maxY-self.CREATION_LIMIT)]
            vector = [random.uniform(-self.SPEED, self.SPEED), random.uniform(-self.SPEED, self.SPEED)]
            bird = Bird(i, position, [maxX/2, maxY/2], vector, maxX, maxY)
            self.birds.append(bird)

    def move(self):
        for bird in self.birds:
            bird.move(self.birds)

    def redirect(self, x, y):
        for bird in self.birds:
            bird.setDesiredPosition(x, y)
