def my_f(**kwargs):
    return ' '.join(kwargs.values())  # Собирает значения в строку
print(my_f(name = input('Введите имя: '), susrname = input('Введите фамилию: '), year = input('Введите год рождения: '),
           city = input('Введите город: '), email = input('Введите email: '), phone_number = input('Введите номер телефона: ')))

'''
        Вариант с использованием lambda  функции.
print((lambda **kwargs: kwargs)(name=input('Введите имя: '), susrname=input('Введите фамилию: '),
                                year=input('Введите год рождения: '),
                                city=input('Введите город: '), email=input('Введите email: '),
                                phone_number=input('Введите номер телефона: ')))'''


