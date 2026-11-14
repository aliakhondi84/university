import math
def phi(z):
    return(1.0/math.sqrt(2*math.pi))*math.exp(-0.5*z**2)
def Phi(z):
    if z >  8.0:  return  1.0
    if z < -8.0: return 0.0
    if z < 0.0: return 1.0 -Phi(-z)
    total=0.0
    term=z
    i=3
    while total !=total+term:
        total += term
        term  *=z*z/float(i)
        i+=2
    return 0.5 +phi(z) * total
def cdf(z, mu=0.0, sigma=1.0):
        return Phi((z-mu)/sigma)
f=cdf(820,1019,209)
print(round(f,5))   