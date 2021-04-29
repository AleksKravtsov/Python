# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл

my_prog = open("test_4.txt", "r", encoding="utf-8")
filestr = my_prog.read()
splitlist = filestr.split("\n")
my_prog.close()

num = []
wordsEN = []
wordsRUS = ["Один","Два","Три","Четыре"]

for line in splitlist:
    wrdsEN, n = line.split("-")
    wordsEN.append(wrdsEN)
    num.append(n)

X_Y = (list(map(lambda x, y: x +" -"+ y+"\n", wordsRUS, num)))

translated = open("Translate_test_4.txt", "w", encoding="utf-8")
translated.write("".join(X_Y))
translated.close()


