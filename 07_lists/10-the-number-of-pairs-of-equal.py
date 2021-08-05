a = [int(i) for i in input().split()]
n = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            n += 1
print(n)