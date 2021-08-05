words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))