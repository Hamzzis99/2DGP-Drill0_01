import turtle

screen = turtle.Screen()
turtle.shape('turtle')

step = 50

def move_up():
    turtle.setheading(90)  
    turtle.stamp()
    turtle.forward(step)
    
    
def move_down():
    turtle.setheading(270)  
    turtle.stamp()
    turtle.forward(step)
    
    
def move_left():
    turtle.setheading(180)  
    turtle.stamp()
    turtle.forward(step)
    
    
def move_right():
    turtle.setheading(0)  
    turtle.stamp()
    turtle.forward(step)
    
def move_reset():
    turtle.reset()
    
    
screen.onkey(move_up, 'w')
screen.onkey(move_down, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(move_reset, 'Escape')


screen.listen()
screen.mainloop()