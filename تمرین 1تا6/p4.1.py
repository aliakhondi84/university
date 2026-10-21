import sys
import random
a=[]
n=int(sys.argv[1])
for i in range(n):
    a += [random.random()]
print(a)