from statistics import median

n = int(input())
a = list(map(int,input().split()))
a.sort()
b , c = [] , []
if n%2==0:
    for i in range(n//2):
        b.append(a[i])
    for i in range(n//2,n):
        c.append(a[i])
else:
    for i in range(n//2):
        b.append(a[i])
    for i in range(n//2+1,n):
        c.append(a[i])
print(int(median(b)))
print(int(median(a)))
print(int(median(c)))
