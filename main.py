from turtle import *

print "Hello"

t = Turtle()

def moveRobot(turt, leftSpeed, rightSpeed):
    if(leftSpeed != rightSpeed):
        if(leftSpeed > rightSpeed):
            r = rightSpeed / leftSpeed
        else:
            r = leftSpeed / rightSpeed

        wr = 49.25 * r
        ic = wr / (1-r)

        mid = ic + 77.3617

        return mid


done()