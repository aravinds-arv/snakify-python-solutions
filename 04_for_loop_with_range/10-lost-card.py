N = int(input())
sum1 = 0
sum2 = 0
for i in range(1,N+1):
    sum1 = sum1 + i
for i in range(1,N):
    sum2 = sum2 + int(input())
print(sum1-sum2)