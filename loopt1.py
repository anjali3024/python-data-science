
#method 2

from turtle import*
speed=(30)
sides = 6
distance = 120
fillcolor("black")
begin_fill()
for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()
mainloop()