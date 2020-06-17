import turtle as t

t.shape('turtle')
for i in range(4):
    t.pensize(5)

t.penup()
t.goto(0,0)
t.pendown()
t.color( 'black' )
t.circle(50)



t.penup()
t.goto(110,0)
t.pendown()
t.color( 'red' )
t.circle(50)


t.penup()
t.goto(-110,0)
t.color( 'blue' )
t.pendown()
t.circle(50)

t.penup()
t.goto(-60,-50)
t.color( 'yellow' )
t.pendown()
t.circle(50)

t.penup()
t.goto(60,-50)
t.color( 'green' )
t.pendown()
t.circle(50)



