import random

while True:
    a = []
    b = row = column = 0
    try:
        column = int(input("Введите количество столбцов: "))
    except ValueError as e:
        print(e)

    try:
        row = int(input("Введите количество строк: "))
    except ValueError as e:
        print(e)

    for i in range(row):
            am = []
            for j in range(column):
                am.append(random.randint(0, 100))
            a.append(am)
    print("\nИсходная матрица:")
    for i in range(len(a)):
        print(a[i])
    for i in range(len(a)):
        sor = 0
        for j in range(len(a[i])-1):
            if a[i][j] >= a[i][j+1]:
                sor = 1
                break
        if sor == 0:
            a[i].reverse()

    print("\nИтоговая матрица:")
    for i in range(len(a)):
        print(a[i])
