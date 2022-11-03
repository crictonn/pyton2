a = input("Введите первую переменную: ")
b = input("Введите вторую переменную: ")
try:
    a = int(a)
    b = int(b)
    print("a / b = ", a/b)
except TypeError as e:
    print(e)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
finally:
    print("Выполнение программы завершено")