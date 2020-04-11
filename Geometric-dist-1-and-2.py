a, b = map(int,input().split())
r = int(input())
r -= 1
p = a/b
q = 1 - p
print(round(p*(q**r),3))

print(round(1 - (1 - (1 / 3))**5, 3))