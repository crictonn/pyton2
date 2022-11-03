a = [[8, 2, 7], [4, 5, 6], [7, 2, 4]]
for i in len(a):
    sor = 0
    for j in len(a[i]):
        if a[i][j] <= a[i][j+1]:
            sor = 1
            break
    if sor == 0:
        b = a[i]


print(b)
