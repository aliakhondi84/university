
import random
import math
A = []
for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    A.append([x,y])
for i in range(10):
    print("A",i+1,"=",A[i],end=" ")
print()
min = 100
for i in range(10):
    for j in range(i+1,10):
        x1 = A[i][0]
        y1 = A[i][1]

        x2 = A[j][0]
        y2 = A[j][1]

        F = math.sqrt((x1-x2)**2 + (y1-y2)**2)

        if F < min:
            min = F
            a = i+1
            b = j+1
print("Between A"+str(a),"and A"+str(b))
print("Shortest distance =",min)