x = 1
while x<5:
    print ("run")
    x+=1
print("stop")


for i in range (1,11):
    if (i==7):
        print("out of loop")
        break
    else:
        print(i)
for i in range(1,9):
    if(i==6):
        continue
    else:
        print(i)

#loop5
fruits = ["apple","banana","orange"]
for fruit in fruits:
    print(fruit)
else:
    print("that's all ")