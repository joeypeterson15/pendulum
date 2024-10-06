from graphics import *
from sympy import symbols, diff
import numpy 
# Pendulum: equation:   
    # torque = τ = I(α) where I = moment of Intertia = mL^2
                          #   α = angular acceleration = d^2(θ) / d(t)^2
    # anglular force = torque = F * (length of pendulum) = -mgsin(θ) * L
    # solving for theta:
    #       d^2(θ) / d(t)^2 + (g/L)sin(θ) = 0

    # with damping:
    #       d^2(θ)/d(t)^2 + (c)d(θ)/d(t) + (g/L)sin(θ) = F(initial)cos(wt)

g = 9.8
pi = 3.14
scalar = 5

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

    def _updateAngularAcceleration(self): # need to update the angle every time we get called(Eulers method)
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
    cols = 300
    rows = 500
    angle = 40
    pendulumLength = 120
    xCenter = rows / 2
    window = GraphWin("pendulum", rows, cols, autoflush=False)

    pendulum = Pendulum(angle, pendulumLength)
    xCoor = xCenter + pendulum.getXCoordinate()
    yCoor = pendulum.getYCoordinate()

    circle = Circle(Point(xCoor, yCoor), 8)
    circle.setFill('pink')
    circle.draw(window)

    pointRotation = Circle(Point(xCenter, 0), 2)
    pointRotation.setFill("pink")
    pointRotation.draw(window)
    aLine = Line(Point(xCenter,0), Point(xCoor, yCoor))
    aLine.draw(window)

    cosTensionForce = Line(Point(xCoor, yCoor), Point(xCoor + g * numpy.sin(pendulum.angle), yCoor + (g * numpy.cos(pendulum.angle))))
    cosTensionForce.draw(window)

    sinForceArrow = Line(Point(xCoor, yCoor), Point(xCenter + g * (numpy.cos(pendulum.angle)), g * -numpy.sin(pendulum.angle)))
    sinForceArrow.draw(window)

    gForceMagnitude = scalar * g
    gForce = Line(Point(xCoor, yCoor), Point(xCoor, yCoor + gForceMagnitude))

    while True:
        pendulum.process()
    
        circle.undraw()
        aLine.undraw()
        sinForceArrow.undraw()
        cosTensionForce.undraw()
        gForce.undraw()

        xPos = xCenter + (pendulum.getXCoordinate())
        YPos = pendulum.getYCoordinate()

        circle = Circle(Point(xPos, YPos), 8)
        aLine = Line(Point(xCenter,0), Point(xPos, YPos))
        aLine.draw(window)
        circle.setFill('pink')
        circle.setOutline('pink')
        circle.draw(window)

        sinForceScalar = scalar * numpy.sin(pendulum.angle)
        sinForceMagnitude = g * sinForceScalar
        sinForceXDirection = -numpy.cos(pendulum.angle) #to make perpendicular, swap the left and right and change the new x negative
        sinForceYDirection = numpy.sin(pendulum.angle)
        sinForceArrow = Line(Point(xPos, YPos), Point(xPos + sinForceXDirection * sinForceMagnitude, YPos + sinForceYDirection * sinForceMagnitude))
        sinForceArrow.setArrow("last")
        sinForceArrow.setOutline("red")
        sinForceArrow.draw(window)

        tensionScalar = scalar * abs(numpy.cos(pendulum.angle))
        cosTensionMagnitude = g * tensionScalar
        cosTensionForce = Line(Point(xPos, YPos), Point(xPos + (cosTensionMagnitude * numpy.sin(pendulum.angle)), YPos + (cosTensionMagnitude * numpy.cos(pendulum.angle))))
        cosTensionForce.setArrow("last")
        cosTensionForce.setOutline("red")
        cosTensionForce.draw(window)

        gForceMagnitude = scalar * g
        gForce = Line(Point(xPos, YPos), Point(xPos, YPos + gForceMagnitude))
        gForce.setArrow("last")
        gForce.setOutline("blue")
        gForce.draw(window) 

        if window.checkMouse():
            break
        window.update()

        time.sleep(0.09)

main()