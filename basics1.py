from statistics import mean,median,mode

n = int(input())
a = list(map(int,input().split()))
print(round(mean(a),1))
print(round(median(a),1))
a.sort()
print(max(a,key=a.count))
