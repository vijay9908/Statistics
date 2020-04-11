from statistics import mean

n = int(input())
a = list(map(int,input().split()))
m = mean(a)
sum = 0
for ele in a:
    sum += (ele-m)**2
sum /= n
print(round(sum**0.5,1))