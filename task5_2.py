n = 20
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    for l in range(i-1, 0, -1):
        print(l, end=" ")
    print()