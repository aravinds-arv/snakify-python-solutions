A = int(input())
B = int(input())
if A < B:
    for x in range(A,B+1):
        print(x, end = " ")
else:
    for x in range(A,B-1,-1):
        print(x, end = " ")