def write():
    a = int(input("Введите число:"))
    if a == 0:
        return
    elif a % 2 == 1:
        print(a)
        write()
    else:
        write()
write()