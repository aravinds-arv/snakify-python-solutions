a = input().split()
n, m = int(a[0]), int(a[1])
a = []
b = ". " * m
for i in range(n):
    a.append(b.split(" "))
for i in range(n):
    for j in range(m):
        if (i+j)%2 != 0:
            a[i][j] = "*"
for i in range(n):
    print(" ".join(a[i]))