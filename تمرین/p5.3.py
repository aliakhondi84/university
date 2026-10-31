import random
import math
A = []
for i in range(10):
    x=random.randint(1,10)
    y=random.randint(1,10)
    A.append([x, y])

for i in range(10):
    print("A",(i + 1),"=",A[i])
    
for i in range(10):
    for j in range(10): 
        x1=A[i][0]
        y1=A[i][1]

        x2=A[j][0]
        y2=A[j][1]       
        F=(math.sqrt((x1-x2)**2)+(y1-y2)**2)
        print("A",i+1,"and A",j+1,"=",F)