
import sys
n=int(sys.argv[1])
a=[]
while n>0:
       x=n%2
       a.append(x)
       n=n//2
for i in reversed(a):
 print(i,end='')



