import sys 
import math
x=int(sys.argv[1])
y=int(sys.argv[2])
def hypot(a,b):
    return math.sqrt(a*a + b*b)
print(hypot(x,y))
