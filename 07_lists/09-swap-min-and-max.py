a = [int(i) for i in input().split()]
max = a[0]
min = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
l = a.index(max)
m = a.index(min)
a[l],a[m] = a[m], a[l]
for i in a:
    print(i, end =" ")