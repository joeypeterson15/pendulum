from graphics import *
from sympy import symbols, diff
import numpy 
# Pendulum: equation:   
    # torque = τ = I(α) where I = moment of Intertia = mL^2
                          #   α = angular acceleration = d^2(θ) / d(t)^2
    # anglular force = torque = F * (length of pendulum) = -mgsin(θ) * L
    # solving for theta:
    #       d^2(θ) / d(t)^2 + (g/L)sin(θ) = 0
g = 9.8
pi = 3.14
frameTime = 0
xShift = 200
yShift = 200

class Pendulum:
    def __init__(self, initAngle, length):
        self.angle = initAngle
        self.length = length
        self.oscillationConst = g / length# not to be confused with angular velocity. 
        self.angVel = 0
        self.angAcc = -g / length * numpy.sin(initAngle)

    def process(self):
        self.updateAngularAcceleration()
        self.updateAngVelocity()
        self.updateAngle()

    def updateAngularAcceleration(self): # need to update the angle every time we get called
        self.angAcc = - self.oscillationConst * numpy.sin(self.angle)
    def updateAngVelocity(self):
        self.angVel += self.angAcc * frameTime
    def updateAngle(self):
        self.angle += self.angVel * frameTime
    def getXCoordinate(self):
        return self.length * numpy.cos(self.angle)
    def getYCoordinate(self):
        return self.length * numpy.sin(self.angle)
        

def main():
    cols = 400
    rows = 400

    window = GraphWin("pendulum", rows, cols, autoflush=False)
    pendulum = Pendulum(20, 100)
    circle = Circle(Point(200 - pendulum.getXCoordinate(), pendulum.getYCoordinate() - 200), 20)
    circle.setFill('pink')
    circle.draw(window)

    while True:
        pendulum.process()
        circle = Circle(Point(200 - pendulum.getXCoordinate(), pendulum.getYCoordinate() - 200), 20)
        circle.undraw()
        circle.draw(window)
        # window.getMouse()
        # window.close()

main()