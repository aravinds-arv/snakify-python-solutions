s = input()
n = len(s)
for i in range(0,n,3):
    s = s.replace(s[i],"%",1)
s = s.replace("%","")
print(s)