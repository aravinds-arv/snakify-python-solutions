n = int(input())
ls = []
for i in range(n):
    a = [[0]*(n-i-1) + [1] + [2] * i]
    ls.append(a)

for i in range(n):
    for j in ls[i]:
        print(' '.join([str(i) for i in j]))