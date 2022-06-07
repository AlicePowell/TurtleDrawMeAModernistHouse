import turtle

turtle.speed(6)
turtle.begin_fill()

houseHeight = 60
roofHeight = 10
houseWidth = 280
roofWidth = 320
rightAngle = 90
isometric1 = 30
isometric2 = 60
isometric3 = 150


def box(width, height, angle1, angle2):
    for front in range(2):
        turtle.forward(width)
        turtle.right(angle1)
        turtle.forward(height)
        turtle.right(angle2)


turtle.color('white')
turtle.forward(60)
turtle.right(180)

# draw roof
# turtle.color('gray', '#d3d3d3')
turtle.color('gray', '#efe5e6')
box(roofWidth, 200, isometric3, isometric1)

turtle.end_fill()

turtle.left(90)
box(roofHeight, roofWidth, rightAngle, rightAngle)

turtle.forward(roofHeight)
turtle.left(120)
turtle.forward(200)
turtle.left(isometric2)
turtle.forward(roofHeight)

turtle.right(180)
turtle.forward(roofHeight)


turtle.right(isometric2)
turtle.forward(200)
turtle.right(isometric1)
turtle.forward(20)
turtle.left(rightAngle)


box(houseHeight, houseWidth, rightAngle, rightAngle)

turtle.forward(houseHeight)
turtle.left(122)
turtle.forward(198)

turtle.left(58)
turtle.forward(40)

turtle.left(180)
turtle.forward(30)

# position for windows
turtle.right(58)
turtle.forward(1)
turtle.color('white')
turtle.forward(24)

# fill windows
turtle.begin_fill()
turtle.color('gray', '#FFFFBF')

turtle.forward(144)
turtle.right(122)
turtle.forward(37)
turtle.right(isometric2)
turtle.forward(141)
turtle.right(120)
turtle.forward(31)

turtle.end_fill()

# draw remaining parts of windows


def windows(distance1, distance2, turn1, turn2):
    turtle.right(turn1)
    turtle.forward(distance1)
    turtle.right(turn2)
    turtle.forward(distance2)
    turtle.right(180)
    turtle.forward(distance2)


for window in range(3):
    perspectiveHeight = window * 3 + 31
    windowLength = window + 47
    windows(windowLength, perspectiveHeight, 58, 122)

# position for picture window
turtle.color('white')
turtle.right(58)
turtle.forward(29)

turtle.color('gray')
turtle.left(58)
turtle.forward(10)
turtle.right(rightAngle)
turtle.forward(20)
turtle.right(rightAngle)
turtle.forward(1)
turtle.left(rightAngle)

# draw picture window
turtle.begin_fill()
turtle.color('gray', '#FFFFBF')
box(130, 58, rightAngle, rightAngle)
turtle.end_fill()

# draw sliding door
turtle.forward(240)
turtle.right(rightAngle)
box(58, 110, rightAngle, rightAngle)

turtle.forward(1)
turtle.right(rightAngle)
turtle.forward(1)
turtle.left(rightAngle)

turtle.begin_fill()
turtle.color('gray', '#FFFACD')
box(56, 108, rightAngle, rightAngle)

turtle.end_fill()

# position for grass
turtle.right(180)
turtle.forward(2)
turtle.right(rightAngle)
turtle.forward(20)
turtle.left(rightAngle)

turtle.color('white')
turtle.forward(16)
turtle.right(rightAngle)
turtle.forward(40)

# grass
turtle.begin_fill()
turtle.color('gray', '#98FB98')
turtle.left(180)
turtle.forward(roofWidth+7)
turtle.left(33)
turtle.forward(230)

# grass
turtle.right(33)
turtle.forward(100)
turtle.right(144)
turtle.forward(600)
turtle.right(36)
turtle.forward(roofWidth + 207)
turtle.right(isometric3)
turtle.forward(453)

turtle.end_fill()


turtle.left(isometric2)
turtle.forward(1)
turtle.color('white')
turtle.forward(300)

turtle.done()
