import turtle




t = turtle.Turtle()
screen = turtle.Screen()


SPEED = 5

#TODO draw field
#TODO implement position tracking code to check points
#TODO add interface of some kind

#field is 360" x 888"
#field mid end 264"
#angles

screen.screensize(1000, 500)
def drawField(turt, startX, startY):
    turt.penup()
    turt.forward(500)
    turt.right(90)

    turt.pendown()

    #outside carpet
    turt.forward(180)
    turt.right(90)
    turt.forward(888)
    turt.right(90)
    turt.forward(360)
    turt.right(90)
    turt.forward(888)
    turt.right(90)
    turt.forward(180)

    turt.penup()

    #outside field wall


def moveRobot(turt, leftSpeed, rightSpeed):
    if(leftSpeed != rightSpeed):
        if(leftSpeed > rightSpeed):
            r = float(rightSpeed) / float(leftSpeed)
        else:
            r = float(leftSpeed) / float(rightSpeed)

        wr = 49.25 * r
        ic = wr / (1-r)

        mid = ic + 77.3617

        amt2turn = (SPEED * 360) / mid

        if(leftSpeed > rightSpeed):
            turt.right(amt2turn)
        else:
            turt.left(amt2turn)

        turt.forward(SPEED)

        return mid
    else:
        turt.forward(SPEED)

drawField(t, 0, 0)

while(True):
    moveRobot(t, 75, 100)

turtle.done()