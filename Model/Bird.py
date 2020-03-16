import numpy as np
import random

class Bird:

    MAX_SPEED = 4
    W_FOLLOW = 0.3 #Weight of follow
    RADIUS = 35

    def __init__(self, id, currentPosition, desiredPosition, vector):
        self.id = id
        self.currentPosition = np.array(currentPosition).astype(float)
        self.desiredPosition = np.array(desiredPosition).astype(float)
        self.follow = np.array([0, 0]).astype(float)
        self.vector = np.array(vector).astype(float)
        self.acceleration = np.array([0, 0]).astype(float)

    def move(self, otherBirds):
        self.resetAcceleration()
        self.follow(otherBirds)
        #self.updateSteer()
        self.updateVect()
        self.currentPosition = np.add(self.currentPosition, self.vector)

    def updateVect(self):
        self.vector = np.add(self.vector, self.acceleration)
        self.vector = self.speedLimit(self.vector, self.MAX_SPEED)

    def updateSteer(self):
        desiredVector = np.subtract(self.desiredPosition, self.currentPosition)
        desiredVector = self.speedLimit(desiredVector, self.MAX_SPEED)

        self.follow = np.subtract(desiredVector, self.vector)
        self.follow = self.speedLimit(self.follow, self.W_FOLLOW)

        self.applyForce(self.follow)

    def resetAcceleration(self):
        self.acceleration = np.zeros(2)

    def applyForce(self, v):
        self.acceleration = np.add(self.acceleration, v)

    def follow(self, otherBirds):
        sumVector = np.array([0, 0]).astype(float)
        closeBirds = 0
        for bird in otherBirds:
            d = self.dist(bird)
            if self.RADIUS >= d > 0 and self.id != bird.id:
                closeBirds += 1
                sumVector = np.add(sumVector, bird.getVector())

        if closeBirds > 0:
            avg = np.divide(sumVector, closeBirds)
            avg = self.speedLimit(avg, self.MAX_SPEED)
            self.follow = np.subtract(avg, self.vector)
            self.follow = self.speedLimit(self.follow, self.W_FOLLOW)
            self.applyForce(self.follow)

    def speedLimit(self, v, limit):
        norm = np.linalg.norm(v)
        if norm > limit:
            v = limit * np.divide(v, norm)
        return v

    def setDesiredPositon(self, x, y):
        self.desiredPosition = np.array([x, y]).astype(float)

    def getVector(self):
        return self.vector

    def dist(self, other):
        vect = np.subtract(other.currentPosition, self.currentPosition)
        return np.linalg.norm(vect)
