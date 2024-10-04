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
xShift = 400
yShift = 400

class Pendulum:
    def __init__(self, initAngle, length):
        self.angle = numpy.radians(initAngle)
        self.length = length
        self.oscillationConst = (g / length)
        self.angVel = 0
        self.angAcc = -(g / length) * numpy.sin(numpy.radians(initAngle))

    def process(self):
        self._updateAngularAcceleration()
        self._updateAngVelocity()
        self._updateAngle()

    def _updateAngularAcceleration(self): # need to update the angle every time we get called
        self.angAcc = -self.oscillationConst * numpy.sin(self.angle)
    def _updateAngVelocity(self):
        self.angVel += self.angAcc
    def _updateAngle(self):
        self.angle += self.angVel

    def getXCoordinate(self):
        return self.length * numpy.sin(self.angle)
    def getYCoordinate(self):
        return self.length * numpy.cos(self.angle)
        

def main():
    cols = 800
    rows = 800

    window = GraphWin("pendulum", rows, cols, autoflush=False)
    pendulum = Pendulum(80, 70)
    circle = Circle(Point(400 + pendulum.getXCoordinate(), pendulum.length + pendulum.getYCoordinate()), 20)
    circle.setFill('pink')
    circle.draw(window)
    pointRotation = Circle(Point(400, 0), 15)
    pointRotation.setFill("pink")
    pointRotation.draw(window)
    aLine = Line(Point(400,0), Point(200 + pendulum.getXCoordinate(), pendulum.length + pendulum.getYCoordinate()))
    aLine.draw(window)

    while True:
        circle.undraw()

        pendulum.process()
        aLine.undraw()
        xPos = 400 + pendulum.getXCoordinate() * 3
        YPos = pendulum.length + pendulum.getYCoordinate() * 3

        circle = Circle(Point(xPos, YPos), 20)
        aLine = Line(Point(400,0), Point(xPos, YPos))
        aLine.draw(window)
        circle.setFill('pink')
        circle.draw(window)

        if window.checkMouse():
            break
        window.update()

        time.sleep(0.1)

main()