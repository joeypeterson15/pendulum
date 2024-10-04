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
# offset = 5
xShift = 200
yShift = 200

class Pendulum:
    def __init__(self, initAngle, length):
        self.offset = 2 #this will be our measure of "time" since we will increment this number on every update
        self.angle = numpy.radians(initAngle)
        self.length = length
        self.oscillationConst = g / length #not to be confused with angular velocity. 
        self.angVel = 0
        self.angAcc = -g / length * numpy.sin(numpy.radians(initAngle))

    def process(self):
        self._updateAngularAcceleration()
        self._updateAngVelocity()
        self._updateAngle()

    def _updateAngularAcceleration(self): # need to update the angle every time we get called
        self.angAcc = - self.oscillationConst * numpy.sin(self.angle)
    def _updateAngVelocity(self):
        self.angVel += self.angAcc * self.offset
    def _updateAngle(self):
        self.angle += self.angVel * self.offset

    def getXCoordinate(self):
        return self.length * numpy.cos(self.angle)
    def getYCoordinate(self):
        return self.length * numpy.sin(self.angle)
        

def main():
    cols = 400
    rows = 400

    window = GraphWin("pendulum", rows, cols, autoflush=False)
    pendulum = Pendulum(20, 20)
    circle = Circle(Point(pendulum.getXCoordinate() + 200, 200 - pendulum.getYCoordinate()), 5)
    circle.setFill('red')
    circle.draw(window)
    c = Circle(Point(50, 200), 40)
    c.setFill('blue')
    c.draw(window)

    counter = 50
    while True:
        circle.undraw()
        pendulum.process()
        circle = Circle(Point(200 + pendulum.getXCoordinate(), 200 - pendulum.getYCoordinate()), 20)
        circle.draw(window)
        # if counter > 25:
        #     print("angle acceleration:", pendulum.angAcc)
        #     print("angle velocity:", pendulum.angVel)
        #     print("angle:", pendulum.angle)

        if window.checkMouse():
            break

        time.sleep(0.5)
        counter = counter - 1

main()