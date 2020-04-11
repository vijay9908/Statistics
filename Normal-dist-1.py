from math import erf 

mean , var = 20 , 2
k1 = 19.5
p1 , p2 = 20,22

def normal(x, mean, var):
        return 0.5 + 0.5 * erf((x-mean)/(var* 2**0.5))

print(normal(k1,mean,var))
print(normal(p2,mean,var)-normal(p1,mean,var))    
