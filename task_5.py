revenue = int(input('Введите значение выручки'))
costs = int(input('Введите значение издержек'))

if revenue < costs:
    print('Вы работаете в убыток!')
elif revenue == costs:
    print('Ваша деятельность выходит в ноль.')
else:
    profit = revenue - costs
    print('Поздравляем, ваша работа приносит прибыль!')
    print('Размер вашей прибыли: ', profit)
    margin = revenue / costs
    print('Ваша рентабельность:', margin)
    workers = int(input('Введите число сотрудников:'))
    income_per_worker = profit / workers
    print('На каждого вашего сотрудника приходится', int(income_per_worker), 'прибыли')