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
# class forceArrow:
        

def main():
    cols = 800
    rows = 800
    window = GraphWin("pendulum", rows, cols, autoflush=False)

    pendulum = Pendulum(40, 120)
    xCoor = 400 + pendulum.getXCoordinate()
    yCoor = pendulum.getYCoordinate()

    circle = Circle(Point(xCoor, yCoor), 8)
    circle.setFill('pink')
    circle.draw(window)

    pointRotation = Circle(Point(400, 0), 2)
    pointRotation.setFill("pink")
    pointRotation.draw(window)
    aLine = Line(Point(400,0), Point(xCoor, yCoor))
    aLine.draw(window)

    upArrowForce = Line(Point(xCoor, yCoor), Point(xCoor - g * numpy.sin(pendulum.angle), yCoor - 5 * g * numpy.cos(pendulum.angle)))
    upArrowForce.setArrow("last")
    upArrowForce.draw(window)

    downTensionForce = Line(Point(xCoor, yCoor), Point(xCoor + g * numpy.sin(pendulum.angle), yCoor + (g * numpy.cos(pendulum.angle))))
    downTensionForce.draw(window)

    forceArrow = Line(Point(xCoor, yCoor), Point(400 + g * (numpy.cos(pendulum.angle)), g * -numpy.sin(pendulum.angle)))
    forceArrow.draw(window)



    while True:
        pendulum.process()
    
        circle.undraw()
        aLine.undraw()
        forceArrow.undraw()
        downTensionForce.undraw()

        xPos = 400 + (pendulum.getXCoordinate())
        YPos = pendulum.getYCoordinate()

        circle = Circle(Point(xPos, YPos), 8)
        aLine = Line(Point(400,0), Point(xPos, YPos))
        aLine.draw(window)
        circle.setFill('pink')
        circle.draw(window)

        forceArrow = Line(Point(xPos, YPos), Point(xPos - 5 * g * numpy.sin(pendulum.angle), YPos + (pendulum.length - YPos)))
        forceArrow.setArrow("last")
        forceArrow.draw(window)

        upArrowForce.undraw()
        upArrowForce  = Line(Point(xPos, YPos), Point(xPos + numpy.cos(pi / 2 + pendulum.angle) * pendulum.length / 2, YPos - numpy.sin(pi / 2 + pendulum.angle) * pendulum.length / 2))
        upArrowForce.setArrow("last")
        upArrowForce.draw(window)

        downTensionForce = Line(Point(xPos, YPos), Point(xPos + g * 5 * numpy.sin(pendulum.angle), YPos + (g * 5 * numpy.cos(pendulum.angle))))
        downTensionForce.setArrow("last")
        # downTensionForce = Line(Point(xPos, YPos), Point((pendulum.length - xPos), YPos + (g * 5 * numpy.cos(pendulum.angle))))
        downTensionForce.draw(window)

        if window.checkMouse():
            break
        window.update()

        time.sleep(0.18)

main()