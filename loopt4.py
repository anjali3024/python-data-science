from turtle import*
speed(6)
pensize(2)
pencolor('purple')
for i in range (17):
    forward(100)
    left(360/5)
    for i in range (14):
        forward(140)
        left(360/6)
        dot(5)

mainloop()