import numpy as np


def speedLimit(v, limit):
    norm = np.linalg.norm(v)
    if norm > limit:
        v = limit * np.divide(v, norm)
    return v


class Bird:
    BORDER_EDGES = 25 #Border of edges in which we are in danger

    MAX_SPEED = 2   #Max magnitude of a vector
    W_FOLLOW = 0.2 # Weight of follow
    W_AVOID = 0.1   # Weight of avoid

    STEER_FORCE = 0.2 #Steering force when close to an edge
    RADIUS = 50     # Perception radius

    def __init__(self, identifier, currentPosition, desiredPosition, vector, edgeX, edgeY):
        self.identifier = identifier

        self.edgeX = edgeX
        self.edgeY = edgeY

        self.currentPosition = np.array(currentPosition).astype(float)
        self.desiredPosition = np.array(desiredPosition).astype(float)

        self.vector = np.array(vector).astype(float)
        self.acceleration = np.array([0, 0]).astype(float)
    #end __init__

    def move(self, otherBirds):
        self.resetAcceleration()
        #See which birds are close to us
        neighbours = self.getNeighbourBirds(otherBirds)
        #First calculate follow vector
        self.follow(neighbours)
        self.avoid(neighbours)
        self.updateVect()
        self.currentPosition = np.add(self.currentPosition, self.vector)
    #end move

    def updateVect(self):
        # We don't want to touch the edges so we add a force to go away from it
        self.awayFromBorders()
        #self.acceleration = speedLimit(self.acceleration, self.MAX_SPEED)
        self.vector = np.add(self.vector, self.acceleration)
        self.vector = speedLimit(self.vector, self.MAX_SPEED)
    #end updateVect

    def resetAcceleration(self):
        self.acceleration = np.zeros(2)
    #end resetAcceleration

    def applyForce(self, v):
        self.acceleration = np.add(self.acceleration, v)
    #end applyForce

    def awayFromBorders(self):
        if self.BORDER_EDGES > self.currentPosition[0] or self.currentPosition[0] > self.edgeX-self.BORDER_EDGES:
            v = np.array([-self.vector[0] * self.MAX_SPEED, self.vector[1]])
            force = self.calculateForce(v, self.STEER_FORCE)
            self.applyForce(force)
        elif self.BORDER_EDGES > self.currentPosition[1] or self.currentPosition[1] > self.edgeY-self.BORDER_EDGES:
            v = np.array([self.vector[0], -self.vector[1] * self.MAX_SPEED])
            force = self.calculateForce(v, self.STEER_FORCE)
            self.applyForce(force)
    #end awayFromBorders

    def calculateForce(self, v, magnitude):
        return np.subtract(v, self.vector)
    #end calculateForce

    def follow(self, neighbours):
        sumVector = np.array([0, 0]).astype(float)
        closeBirds = len(neighbours)
        for bird in neighbours:
            sumVector = np.add(sumVector, bird.getVector())

        if closeBirds > 0:
            avg = np.divide(sumVector, closeBirds)
            avg = speedLimit(avg, self.MAX_SPEED/2)
            followVector = self.calculateForce(avg, self.W_FOLLOW)
            self.applyForce(followVector)
    #end follow

    def avoid(self, neighbours):
        sumVector = np.array([0, 0]).astype(float)
        closeBirds = len(neighbours)
        for bird in neighbours:
            separate = np.subtract(self.currentPosition, bird.currentPosition)
            sumVector = np.add(sumVector, separate)

        if closeBirds > 0:
            avg = np.divide(sumVector, closeBirds)
            avg = speedLimit(avg, self.MAX_SPEED)
            avoidVector = self.calculateForce(avg, self.W_AVOID)
            self.applyForce(avoidVector)
    #end avoid

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
