a = [int(i)for i in input().split()]
n = 1
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        n += 1
print(n)