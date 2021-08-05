x = int(input())
lst = []

while x != 0:
  lst.append(x)
  x = int(input())

lst = [int(x) for x in lst]
lst.sort()

print(lst[-2])