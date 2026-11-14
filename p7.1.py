import sys
def is_prime(n):
    if n<2:
        return False
    i=2
    while i*i <=n:
        if n%i==0:
           return False
        i+=1
    return True
if len(sys.argv)>1:
   number=int(sys.argv[1])
   print(is_prime(number))
else:
    print()
