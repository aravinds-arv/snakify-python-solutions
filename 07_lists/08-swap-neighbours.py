a = [int(i) for i in input().split()]
n = 0
for i in range(int(len(a)/2)):
    a[n],a[n+1] = a[n+1],a[n]
    n += 2
for i in a:
    print(i, end = " ")