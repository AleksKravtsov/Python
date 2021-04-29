# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_prog = open("test_2.txt", "r", encoding="utf-8")

filestr = my_prog.read()

splitlist = filestr.split("\n")  #Количество строк
wc=[]#word count

for n in splitlist:
    "Добавляет длину каждого элемента в списке"
    wc.append(len(n.split(" ")))

X_Y = list(map(lambda x, y: (x, y), wc, range(1,(len(splitlist))+1)))

for x,y in X_Y:
    print(f"In line - {y} there is - {x} words")
print(f"Total amount of lines is - {len(splitlist)}")

my_prog.close()

''' Не очень красивый вариант
my_prog = open("test_2.txt", "r", encoding="utf-8")
content = my_prog.read()
print(content)

splitlist = content.split("\n")
print(splitlist)
print(f"Количество строк в файле: {len(splitlist)}")
# print("Мы находимся на позиции: ", my_prog.tell())

my_prog.seek(0)
first_line = my_prog.readline()
fir_words = first_line.split()
print(f"Количество слов в первой строке: {len(fir_words)}")

second_line = my_prog.readline()
sec_words = second_line.split()
print(f"Количество слов во второй строке: {len(sec_words)}")

third_line = my_prog.readline()
thr_words = third_line.split()
print(f"Количество слов в третьей строке: {len(thr_words)}")

four_line = my_prog.readline()
fur_words = four_line.split()
print(f"Количество слов в четвертой строке: {len(fur_words)}")
my_prog.close()'''


'''
Пробовал через цикл
while True:
    my_prog.seek(0)
    # print("Мы находимся на позиции: ", my_prog.tell())
    line = my_prog.readline()
    if line != True:
        words = line.split()
        print(f"Количество слов в первой строке: {len(line)}")
        print("Мы находимся на позиции: ", my_prog.tell())
        
    else:
        break'''

