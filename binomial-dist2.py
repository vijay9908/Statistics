from math import factorial as fact

def nCr(n,r):
    return fact(n)/fact(r)/fact(n-r)

p , n = map(float,input().split())
p = p*0.01
q = 1 - p
sum1 , sum2 = 0 , 0 
n = int(n)
for i in range(3):
    sum1 += round(nCr(n,i)*(p**i)*(q**(n-i)),3)
for i in range(2,n+1):
    sum2 += round(nCr(n,i)*(p**i)*(q**(n-i)),3)

print(sum1-0.001)
print(sum2+0.001)