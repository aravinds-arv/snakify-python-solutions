n = int(input())
a = n
len1 = 1
list1 = []
while n != 0:
    n = int(input())
    if n == a:
        len1 += 1
    else:
        a = n
        len1 = 1
    list1.append(len1)
print(max(list1))