# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
#     Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
#     Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def generator(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp

import json

with open("new_test_7.json", "w", encoding="utf-8") as new_f:
    with open("test_7.txt", "r", encoding="utf-8") as my_f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_f }
        result = [int(i) for i in profit.values() if int(i) > 0]
        average_profit = [profit, {"average_profit": round(sum(result) / len(result))}]
        json.dump(average_profit, new_f, ensure_ascii=False, indent=4)


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n"))
for a in generator(n):
    print(a)

from math import factorial as fact
print(fact(10))