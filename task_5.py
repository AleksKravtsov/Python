# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран

my_prog = open("test_5.txt", "w", encoding="utf-8")
str_list = ["1 14 25 45 30 3 10"]
my_prog.writelines(str_list)
print(str_list)
for line in str_list:
    numbers = line.split(' ')
    print(sum(map(int, numbers)))
my_prog.close()