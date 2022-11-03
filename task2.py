def get_list():
    arg = input("Введите список: ")
    k = arg.split()
    result = [int(item) for item in k]
    return result


def get_tuple():
    arg = input("Введите кортеж: ").split()
    result = [int(item) for item in arg]
    k = tuple(result)
    return k


def get_int():
    arg = int(input("Введите целое число: "))
    return arg


def get_str():
    arg = input("Введите строку: ")
    return arg


def my_func(arg):
    if str(type(arg)) == "<class 'list'>":
        i = zeroAmmount = 0
        while i < len(arg):
            if arg[i] == 0:
                if zeroAmmount == 0:
                    firstZero = i
                if zeroAmmount == 1:
                    secondZero = i
                zeroAmmount += 1
            i += 1
        if zeroAmmount == 0:
            print("Нет нулей")
        elif zeroAmmount == 1:
            print("Всего один ноль")
        elif zeroAmmount > 1:
            summ = 0
            while firstZero < secondZero:
                summ += arg[firstZero]
                firstZero += 1
            print(summ)
    elif str(type(arg)) == "<class 'tuple'>":
        ma = max(arg)
        mi = min(arg)
        lst = list(arg)
        for i in range(len(lst)):
            if lst[i] == ma:
                lst[i] = mi
            elif lst[i] == mi:
                lst[i] = ma
        res = tuple(lst)
        print(res)
    elif str(type(arg)) == "<class 'int'>":
        summ = 0
        while arg != 0:
            if (arg % 10) % 2 == 0:
                summ += arg % 10
            arg = arg // 10
        print(summ)
    elif str(type(arg)) == "<class 'str'>":
        ustr = ""
        sps = arg.split()
        print(sps)
        for i in range(len(arg)):
            print(ord(arg[i]))


while True:
    print("1. Ввод списка\n"
          "2. Ввод кортежа\n"
          "3. Ввод целого числа\n"
          "4. Ввод строки\n"
          "5. Выход\n")
    a = 0
    b = input("Введите выбор: ")
    try:
        a = int(b)
    except ValueError as e:
        print(e)
    if a == 1:
        my_func(get_list())
    elif a == 2:
        my_func(get_tuple())
    elif a == 3:
        my_func(get_int())
    elif a == 4:
        my_func(get_str())
    elif a == 5:
        break