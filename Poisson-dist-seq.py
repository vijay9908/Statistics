from math import exp as e
from math import factorial as fact

o = float(input())
x = int(input())

def pois(o,x):
    return (((o**x)*(e(-o)))/ fact(x))

######################################
print(round(pois(o,x),3))

sumA , sumB = 160 , 128 
sumA += 40*(0.88+0.88**2)
sumB += 40*(1.55+1.55**2)
print(round(sumA,3))
print(round(sumB,3))