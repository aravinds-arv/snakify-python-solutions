list = []
i = int(input())
while i != 0:
    list.append(i)
    i = int(input())
max =max(list)
print(list.index(max) + 1)