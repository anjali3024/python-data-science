orderamt = float(input("enter your expenses"))
choose = input('want to pay with credit card')
if orderamt>1000:
    orderamt = orderamt-(orderamt*3/100)
if choose =="yes":
    orderamt-=100
orderamt+= orderamt * .18
print(orderamt)