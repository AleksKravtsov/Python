# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class divisions_by_zero(Exception):
    def __init__(self, a):
        self.a = a


result = lambda x, y: x / y if y != 0 else divisions_by_zero('Ошибка дедения на 0!!')

print(result(int(input('Введите первое значение: ')), int(input('Введите второе значение: '))))
print(result(int(input('Введите первое значение: ')), int(input('Введите второе значение: '))))




