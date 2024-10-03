from graphics import *
import numpy 
# Pendulum: equation:   
    # torque = τ = I(α) where I = moment of Intertia = mL^2
                          #   α = angular acceleration = d^2(θ) / d(t)^2
    # anglular force = torque = F * (length of pendulum) = -mgsin(θ) * L
    # solving for theta:
    #       d^2(θ) / d(t)^2 + (g/L)sin(θ) = 0
g = 9.8
pi = 3.14
class pendulum:
    def __init__(self, initAngle, mass, length, frequency):
        self.angle = initAngle
        self.mass = mass
        self.length = length
        self.angFreq = frequency * 2 * pi
        self.angle = 
        # φ = arctan(ω₀ / (θ₀ √(g/L)))
        self.offset =  numpy.arctan((self.angFreq / initAngle) * numpy.sqrt(g / length))

    def process(self): # need to update the angle every time we get called
        self.angle += self.offset
        

def main():
    cols = 400
    rows = 400

    window = GraphWin("pendulum", rows, cols, autoflush=False)
    window.plot(200, 200, "black")


    window.getMouse()
    window.close()


main()