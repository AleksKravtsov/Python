def my_f(num_1, num_2):
    dev = num_1 / num_2
    return dev
try:
    print(my_f(int(input("Введите первое значение: ")), int(input("Введите второе значение: "))))

except ZeroDivisionError:  # Перехватываем исключение деления на 0
    print('Devision Error, try next time ;)')


'''def my_f(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print('Devision Error, try next time ;)')
print(my_f(int(input("Введите первое значение: ")), int(input("Введите второе значение: "))))'''







