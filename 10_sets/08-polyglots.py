n = int(input())
num = [0] * n
langs = []
for i in range(n):
    num[i] = int(input())
    lang = set()
    for j in range(num[i]):
        lang.add(input())
    langs.append(lang)

uni = set.union(*langs)
inter = set.intersection(*langs)
print(len(inter))
print("\n".join(sorted(inter)))
print(len(uni))
print("\n".join(sorted(uni)))