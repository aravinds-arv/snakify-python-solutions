n = int(input())
a = 0
b = 1
c = 1
ind = 1
while c < n:
    c = a + b
    a = b
    b = c
    ind += 1
if c != n:
        print(-1)
else:
    print(ind)