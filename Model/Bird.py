import numpy as np


class Bird:

    MAX_SPEED = 5
    RADIUS = 6

    def __init__(self, currentPosition, desiredPosition, vector):
        self.currentPosition = np.array(currentPosition).astype(float)
        self.desiredPosition = np.array(desiredPosition).astype(float)
        self.vector = np.array(vector).astype(float)
        self.acceleration = np.array([0, 0]).astype(float)

    def move(self):
        self.currentPosition += self.vector
        self.updateVect()
        self.updateAcceleration()

    def updateVect(self):
        self.vector += self.acceleration

    def updateAcceleration(self):
        self.acceleration

    def avoid(self, otherBirds):
        sumVector = [0, 0]
        for bird in otherBirds:
            sumVector += bird.getVector()
        avgVector = sumVector/len(otherBirds)

    def setDesiredPositon(self, x, y):
        self.desiredPosition = [x, y]

    def getVector(self):
        return self.vector