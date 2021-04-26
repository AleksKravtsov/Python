# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

'''from itertools import permutations
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = permutations(my_list, 3)

print(*(new_list))'''

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# used = set()
# unique = [x for x in my_list if x not in used and (used.add(x) or True)]
# print(unique)
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
from collections import Counter
counter = Counter(my_list)
new_list = [x for x,n in counter.items() if n==1]
print(new_list)

# unique = list(counter)
# print(unique)

single = [x for x,n in counter.items() if n==1]
print(single)
