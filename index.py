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
dampingCoefficient = 1 / 50

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

    def _updateAngularAcceleration(self): # Eulers method - use previous angle(changing with implicit time in frame change) and previous angle velocity for intial conditions
        self.angAcc = -self.oscillationConst * numpy.sin(self.angle) - (dampingCoefficient * self.angVel)
    def _updateAngVelocity(self):
        self.angVel += self.angAcc
    def _updateAngle(self):
        self.angle += self.angVel

    def getXCoordinate(self):
        return self.length * numpy.sin(self.angle)
    def getYCoordinate(self):
        return self.length * numpy.cos(self.angle)        

def main():
    cols = 200
    rows = 500
    angle = 40
    pendulumLength = 120
    xCenter = rows / 2
    potE_x = rows - rows / 5
    potE_y = pendulumLength - 10 + 5 * g
    kinE_x = rows - rows / 7
    kinE_y = pendulumLength - 10 + 5 * g
    totE_x = rows - rows / 15
    totE_y = pendulumLength - 10 + 5 * g

    yLabelsin = pendulumLength -75 + 5 * g
    yLabelcos = pendulumLength -50 + 5 * g
    yLabelTotal = pendulumLength -25 + 5 * g
    xLabel = rows / 7
    window = GraphWin("pendulum", rows, cols, autoflush=False)

    sinForceLabel = Text(Point(xLabel, yLabelsin), "-g*sin(θ)")
    cosForceLabel = Text(Point(xLabel, yLabelcos), "g*cos(θ)")
    gForceLabel = Text(Point(xLabel, yLabelTotal), "-g")
    cosForceLabel.setTextColor("purple")
    cosForceLabel.setSize(15)
    sinForceLabel.setSize(15)
    gForceLabel.setSize(15)
    sinForceLabel.setTextColor("red")
    gForceLabel.setTextColor("blue")
    sinForceLabel.draw(window)
    cosForceLabel.draw(window)
    gForceLabel.draw(window)
    gForceLabel

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

    initHeight = pendulum.length * (1 - numpy.cos(pendulum.angle))
    potE = g * initHeight #potential energy at initial angle is the maximum potential energy = initial potential energy
    potELine = Line(Point(potE_x, potE_y), Point(potE_x, potE_y - potE))
    potELine.draw(window)

    kinE = 0.5 * (pendulum.length * pendulum.angVel) ** 2
    kinELine = Line(Point(kinE_x, kinE_y), Point(kinE_x, kinE_y - kinE))
    kinELine.draw(window)

    totE = potE + kinE
    totELine = Line(Point(totE_x, totE_y), Point(totE_x, totE_y - totE))
    totELine.draw(window)

    totEText = Text(Point(totE_x, totE_y + 10), "Total")
    totEText.draw(window)

    potEText = Text(Point(potE_x, potE_y + 10), "PE")
    potEText.draw(window)

    kinEText = Text(Point(kinE_x, kinE_y + 10), "KE")
    kinEText.draw(window)

    while True:
        pendulum.process()
    
        circle.undraw()
        aLine.undraw()
        sinForceArrow.undraw()
        cosTensionForce.undraw()
        gForce.undraw()
        kinELine.undraw()
        potELine.undraw()
        totELine.undraw()

        xPos = xCenter + (pendulum.getXCoordinate())
        YPos = pendulum.getYCoordinate()

        circle = Circle(Point(xPos, YPos), 9)
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
        cosTensionForce.setOutline("purple")
        cosTensionForce.draw(window)

        gForceMagnitude = scalar * g
        gForce = Line(Point(xPos, YPos), Point(xPos, YPos + gForceMagnitude))
        gForce.setArrow("last")
        gForce.setOutline("blue")
        gForce.draw(window)

        h = pendulum.length * (1 - numpy.cos(pendulum.angle)) # height is distance from equilibrium height
        potE = (g * h) / 2 #potential energy at initial angle is the maximum potential energy = initial potential energy
        potELine = Line(Point(potE_x, potE_y), Point(potE_x, potE_y - potE))
        potELine.setOutline("orange")
        potELine.setWidth(10)
        potELine.draw(window)

        kinE = (0.5 * (pendulum.length * pendulum.angVel) ** 2) / 2
        kinELine = Line(Point(kinE_x, kinE_y), Point(kinE_x, kinE_y - kinE))
        kinELine.setOutline("green")
        kinELine.setWidth(10)
        kinELine.draw(window)

        totE = potE + kinE
        totELine = Line(Point(totE_x, totE_y), Point(totE_x, totE_y - totE))
        totELine.setWidth(10)
        totELine.draw(window)

        if window.checkMouse():
            break
        window.update()

        time.sleep(0.09)

main()