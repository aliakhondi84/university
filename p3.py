import sys
import math
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
delta=(b**2)-(4*a*c)
if delta>=0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
if delta<0: 
    x1=(-b+ 1j* math.sqrt(-delta))/(2*a)
    x2=(-b- 1j* math.sqrt(-delta))/(2*a)

print(x1)
print(x2)
