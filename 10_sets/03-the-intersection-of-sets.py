a = set(input().split()) & set(input().split())
b = []
for i in a:
    b.append(int(i))
b.sort()
print(" ".join(str(i) for i in b))