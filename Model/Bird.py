import numpy as np


def speedLimit(v, limit):
    norm = np.linalg.norm(v)
    if norm > limit:
        v = limit * np.divide(v, norm)
    return v


class Bird:
    MAX_SPEED = 4   #Max magnitude of a vector
    W_FOLLOW = 0.3  # Weight of follow
    RADIUS = 35     # Perception radius

    def __init__(self, identifier, currentPosition, desiredPosition, vector):
        self.identifier = identifier

        self.currentPosition = np.array(currentPosition).astype(float)
        self.desiredPosition = np.array(desiredPosition).astype(float)

        self.followVector = np.array([0, 0]).astype(float)
        self.vector = np.array(vector).astype(float)
        self.acceleration = np.array([0, 0]).astype(float)
    #end __init__

    def move(self, otherBirds):
        self.resetAcceleration()
        neighbours = self.getNeighbourBirds(otherBirds)
        self.follow(neighbours)
        self.updateVect()
        self.currentPosition = np.add(self.currentPosition, self.vector)
    #end move

    def updateVect(self):
        self.vector = np.add(self.vector, self.acceleration)
        self.vector = speedLimit(self.vector, self.MAX_SPEED)
    #end updateVect

    def resetAcceleration(self):
        self.acceleration = np.zeros(2)
    #end resetAcceleration

    def applyForce(self, v):
        self.acceleration = np.add(self.acceleration, v)
    #end applyForce

    def follow(self, neighbours):
        sumVector = np.array([0, 0]).astype(float)
        closeBirds = len(neighbours)
        for bird in neighbours:
            sumVector = np.add(sumVector, bird.getVector())

        if closeBirds > 0:
            avg = np.divide(sumVector, closeBirds)
            avg = speedLimit(avg, self.MAX_SPEED)
            self.followVector = np.subtract(avg, self.vector)
            self.followVector = speedLimit(self.followVector, self.W_FOLLOW)
            self.applyForce(self.followVector)
    #end follow

    def setDesiredPosition(self, x, y):
        self.desiredPosition = np.array([x, y]).astype(float)
    #end setDesiredPosition

    def getVector(self):
        return self.vector
    #end getVector

    def dist(self, other):
        vect = np.subtract(other.currentPosition, self.currentPosition)
        return np.linalg.norm(vect)
    #end dist

    def getNeighbourBirds(self, otherBirds):
        neighbours = []
        for bird in otherBirds:
            d = self.dist(bird)
            if self.RADIUS >= d > 0 and self.identifier != bird.identifier:
                neighbours.append(bird)
        return neighbours
    #end getNeighbourBirds
