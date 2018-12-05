from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

speed(0)

for index, colour in enumerate(colors):
    color(colour, colour)
    begin_fill()
    for i in range(2):
        forward(100)
        right(90)
        forward(200)
        right(90)
    forward(100)   
    end_fill() 

mainloop()