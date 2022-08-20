from turtle import*

colors = ['red','blue','green','purple']
pensize(30)
for i in range (90):
    pencolor(colors[i%4])
    forward(200)
    left(360/3)
    forward(200)
    left(360/30)
    dot(i*10)
mainloop()