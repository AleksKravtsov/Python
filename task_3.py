def my_func(num_1, num_2, num_3):
    '''
        Возвращение суммы наибольших аргументов
    my_func(num_1, num_2, num_3) -> list
    В новом списке all_numbers находим минимальное значение и убираем его с помощью встроенных функций
    Далее через sum получаем сумму оставшихся значений
    '''
    all_numbers = [num_1, num_2, num_3]
    all_numbers.remove(min(num_1, num_2, num_3))   # Убирает минимальное значение
    return sum(all_numbers)

print(my_func(7, 6, 12))

help(my_func)