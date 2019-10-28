

import turtle


turtle.up()
turtle.shape('turtle')
turtle.goto(0,0)
turtle.color('black', 'black')
turtle.down()
#losange noir
turtle.begin_fill()
turtle.right(0)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill() # remplissage
#losange bleu
turtle.color('blue', 'blue')
turtle.begin_fill()
turtle.right(60)
turtle.forward(100)
turtle.right(60+180)
turtle.forward(100)
turtle.right(120+180)
turtle.forward(100)
turtle.right(60+180)
turtle.forward(100)
turtle.end_fill() # remplissage

#losange rouge
turtle.color('red', 'red')
turtle.begin_fill()
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill() # remplissage

turtle.hideturtle()
turtle.done()

