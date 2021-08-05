a = [int(i) for i in input().split()]
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(max, a.index(max))