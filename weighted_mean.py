n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = sum(b)
q = 0
for ele1,ele2 in zip(a,b):
    q += ele1*ele2
print(round(q/k,1))