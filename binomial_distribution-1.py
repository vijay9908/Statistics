from math import factorial as fact

def nCr(n,r):
    return fact(n)/fact(r)/fact(n-r)

p , q = map(float,input().split())
p = p/(p+q)
q = 1-p
sum = 0
for i in range(3,7):
    sum += round(nCr(6,i)*(p**i)*(q**(6-i)),3)
print(sum)