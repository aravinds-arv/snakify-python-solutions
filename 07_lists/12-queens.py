a = []
for i in range(8):
    ls = [int(i) for i in input().split()]
    a.append(ls)
n = 0
for i in range(8):
    for j in range(i+1,8):
        if abs(a[i][1]-a[j][1]) == abs(a[i][0]-a[j][0]):
            n += 1
        elif abs(a[i][1]-a[j][1]) == 0 or abs(a[i][0]-a[j][0]) == 0:
            n += 1
        else:
            n += 0
if n == 0:
    print("NO")
else:
    print("YES")