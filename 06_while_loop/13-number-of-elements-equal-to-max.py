max = 0
element = -1
s = ""
n = 0
while element != 0:
    element = int(input())
    if element >= max:
        max = element
        n = str(max)
        s = s + "%"+ n + "%"
print(s.count(str(max)))