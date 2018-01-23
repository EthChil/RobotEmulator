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

#324 x 648

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
    turt.right(90)
    turt.forward(120)
    turt.left(90)
    turt.pendown()

    turt.forward(162)
    turt.right(90)
    turt.forward(648)
    turt.right(90)
    turt.forward(324)
    turt.right(90)
    turt.forward(648)
    turt.right(90)
    turt.forward(162)

    turt.penup()
    turt.right(90)
    turt.forward(140)
    turt.pendown()

    #first switch
    turt.left(90)
    turt.forward(76.75)
    turt.right(90)
    turt.forward(56)
    turt.right(90)
    turt.forward(153.5)
    turt.right(90)
    turt.forward(56)
    turt.right(90)
    turt.forward(76.75)

    #plates
    turt.forward(36)
    turt.right(90)
    turt.forward(56)
    turt.right(90)
    turt.forward(72)
    turt.right(90)
    turt.forward(56)
    turt.right(90)
    turt.forward(36)

    turt.penup()
    turt.forward(159.5)
    turt.pendown()

    #scale




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