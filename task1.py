def delit():
    a = k = 0
    a = int(input("Введите число: "))
    while k <= a/2:
        try:
            res = a / k
            ires = int(res)
        except ZeroDivisionError as e:
            print(e)
        else:
            if res == ires:
                print(ires)
        finally:
            k = k + 1


delit()
