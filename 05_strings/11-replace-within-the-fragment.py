s = input()
n1 = s.find("h")
n2 = s.rfind("h")
r = s[n1+1:n2].replace("h", "H")
t = s[:n1+1]
u = s[n2:]
print(t+r+u)