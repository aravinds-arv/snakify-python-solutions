def capitalize(a):
    st = a.split(" ")
    nst = []
    for i in range(len(st)):
        b = st[i]
        c = b[0].upper() + b[1:len(st[i])]
        nst.append(c)
    return(" ".join(nst))

print(capitalize(input()))