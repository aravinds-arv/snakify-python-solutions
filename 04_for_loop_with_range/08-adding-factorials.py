n = int(input())
product = 1
add = 0

for x in range(1, n+1):
    product *= x
    add += product
    
print(add)