import turtle
turtle.goto(0,0)
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
SPACE = 4
direction = None

def up():
    global direction
    direction = UP
    turtle.color('green')
    on_move()
    turtle.setheading(90)
turtle.onkey(up, "Up")

#make turtle go uo
    
def down():
    global direction
    direction = DOWN
    turtle.color('yellow')
    on_move()
    turtle.setheading(180)
turtle.onkey(down,'Down')

#make turtle go down

def right():
    global direction
    direction = RIGHT
    turtle.color('blue')
    on_move()
    turtle.setheading(270)
turtle.onkey(right,'Right')

#make turtle go right

def left():
    global direction
    direction = LEFT
    turtle.color('red')
    on_move()
    turtle.setheading(360)
turtle.onkey(left,'Left')

#make turtle go left

def space():
    global direction
    turtle.penup()
    turtle.onkey(space,'Space')
    on_move()
turtle.listen()

   
def on_move():
    #to do
    global direction
    if direction == UP:
        x,y = turtle.pos()
        turtle.goto(x, y + 20)
    elif direction == DOWN:
        x,y = turtle.pos()
        turtle.goto(x, y -20)
    elif direction == RIGHT:
        x,y = turtle.pos()
        turtle.goto(x + 20, y)
    elif direction == LEFT:
        x,y = turtle.pos()
        turtle.goto(x - 20, y)
  

turtle.mainloop()
