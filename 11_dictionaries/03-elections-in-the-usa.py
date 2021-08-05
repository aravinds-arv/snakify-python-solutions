n = int(input())
d = {}
for i in range(n):
    key, val = input().split()
    if key in d:
        d[key] += int(val)
    else:
        d[key] = int(val)
for key, val in sorted(d.items()):
   print(key, val)