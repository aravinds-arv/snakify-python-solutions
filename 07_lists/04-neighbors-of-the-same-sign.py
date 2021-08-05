st = input().split()
for i in range(len(st)-1):
    if int(st[i]) * int(st[i+1]) > 0:
        print(st[i], st[i+1], end = " ")
        break