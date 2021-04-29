# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

print(argv)

name, virt, rev, prim = argv
zp = argv[1:]
for i in range(len(zp)):
    old_value = zp[i]
    new_value = int(old_value)
    zp[i] = new_value
a = zp[0]
b = zp[1]
c = zp[2]

print(a*b+c)


# my_prog = open("test.txt", "w", encoding="utf-8")
# my_prog.write(f"{input('Введите ваше имя: ')} {input('Введите вашу фамилию: ')} {input('Введите ваш возраст: ')}")
# my_prog.close()

my_prog = open("test_1.txt", "w", encoding="utf-8")
while True:
    x = input('Введите свои данные: ')
    if x != '':
        my_prog = open("test_1.txt", "a", encoding="utf-8")
        my_prog.write(f"{x}\n")

    else:
        break
    my_prog.close()






