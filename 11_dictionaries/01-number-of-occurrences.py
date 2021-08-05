words = input().split()
for i in range(len(words)):
    print(words[:i].count(words[i]), end=' ')