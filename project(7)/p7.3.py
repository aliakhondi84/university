import sys
def harmonic(n,r=1):
    total=0.0
    for i in range(1,n+1):
        total += 1.0 / (i**r)
    return total
for i in range(1, len(sys.argv)):
    arg=int(sys.argv[i])
    value=harmonic(arg)
    print(value)