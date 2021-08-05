a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end = " ")