# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="Drawing things"):
        self.title = title

    def draw(self):
        print(f"Start drawing. {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with. {self.title} pen. ")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with. {self.title} pencil. ")

class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with. {self.title} marker. ")

start = Stationery()
start.draw()
pen = Pen("Black")
pen.draw()
pencil = Pencil("Союз")
pencil.draw()
marker = Marker("Green")
marker.draw()