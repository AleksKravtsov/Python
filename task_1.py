# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка

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






