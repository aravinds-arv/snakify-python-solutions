s = input()
n1 = s.find("h")
n2 = s.rfind("h")
if n2 == len(s)-1:
    s = s.replace(s[n1+1:n2],s[n2-1:n1:-1])
else:
    s = s.replace(s[n1:n2+1],s[n2:n1-1:-1])
print(s)