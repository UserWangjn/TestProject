import turtle

t = turtle.Pen()
t.speed(0)
colors = ['red','green','blue']

for i in range(1,20):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(colors[i%len(colors)])
    t.circle(i*10)


turtle.done()