import turtle

Screen = turtle.Screen()
t = turtle.Turtle() 
t.shape('turtle') 
t.speed(0)
turtle.pensize(5)

def draw_heart_curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
        
t.color('pink', 'pink')

t.begin_fill()

t.left(140)
t.forward(111.65)
draw_heart_curve()

t.left(120)
draw_heart_curve()
t.forward(111.65)

t.end_fill()


style = ('Helvetica Neue', 24, 'italic')
turtle.write('Happy Valentine\'s Day', font=style, align='center')


t.hideturtle()
turtle.done()