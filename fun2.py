import turtle
turtle.goto(0,0)
UP = 0
DOWN = 1
direction = None

def up():
    global direction
    print("You pressed the up key.")
    direction = UP    
turtle.onkey(up, "Up") 
def down():
    global direction
    print('you pressed the down key.')
    direction = DOWN
turtle.onkey(down,'Down')
turtle.listen()

turtle.mainloop()
