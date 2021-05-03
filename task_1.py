# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    # atributes
    __color = "Color"

    def running(self):
        while True:
            print("TrafficLight is Red! STOP!")
            sleep(7)
            print("TrafficLight is Yellow! GET READY!")
            sleep(2)
            print("TrafficLight is Green! GO!")
            sleep(5)
            print("TrafficLight is Yellow! GET READY!")
            sleep(2)

trLight = TrafficLight()
trLight.running()






