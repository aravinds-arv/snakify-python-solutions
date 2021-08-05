N = int(input())
x = 0
m = 1
while m <= N:
    x += 1
    m *= 2
print(x-1, m//2)