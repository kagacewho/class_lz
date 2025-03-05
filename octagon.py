
import matplotlib.patches  # Импортируем модуль для работы с графиками
import matplotlib.pyplot as plt
import math


class Octagon:  # Создаем класс октагон
    def __init__(self, side):
        self.side = side
        self.k = (1 + math.sqrt(2))
        self.corner = 135

    def square(self):  # Вычисления площади октагона
        self.squareoctagon = 2 * self.side**2 * self.corner
        print(f'Площадь октагона равна:  {self.square}')

    def perimeter(self):  # Вычисления периметра октагона
        self.perimeteroctagon = 8 * self.side
        print(f'Периметр октагона равен: {self.perimeter}')

    def circumcircle(self):  # вычисления описанной окружности
        self.radiusccl = self.side * math.sqrt(self.k / (self.k - 1))
        self.squareccl = self.radiusccl**2 * 3.14
        print(f'Радиус описанной окружности равен: {self.radiusccl}')
        print(f'Площадь описанной окружности равен: {self.squareccl}')

    def inscribedcircle(self):  # Вычисления вписанной окружности
        self.radiusicl = (math.sqrt(2) / 2) * self.side
        self.squareicl = self.radiusicl**2 * 3.14 
        print(f'Радиус вписанной окружности равен: {self.radiusicl}')
        print(f'Площадь вписанной окружности равен: {self.squareicl}')

    def graph(self):  # Построения графика октагона
        self.squareoctagon = 2 * self.k * self.side**2
        self.radiusicl = math.sqrt(self.squareoctagon / 8 / (math.sqrt(2) - 1))
        self.radiusccl = math.sqrt(self.squareoctagon / 2 / math.sqrt(2))

        plt.xlim(-20, 20)  # Ось X
        plt.ylim(-20, 20)  # Оси Y
        plt.grid()
        axes = plt.gca()

        oct = matplotlib.patches.Polygon([
            (self.radiusicl, self.side / 2), 
            (self.radiusicl, -self.side / 2),
            (self.side / 2, -self.radiusicl),
            (-self.side / 2, -self.radiusicl),
            (-self.radiusicl, -self.side / 2),
            (-self.radiusicl, self.side / 2), 
            (-self.side / 2, self.radiusicl), 
            (self.side / 2, self.radiusicl)], 
            fill=False, color='black')

        circle1 = matplotlib.patches.Circle((0, 0), radius=self.radiusccl, fill=False, color='green')  
        circle2 = matplotlib.patches.Circle((0, 0), radius=self.radiusicl, fill=False, color='red')

        axes.add_patch(circle1)
        axes.add_patch(circle2)
        axes.add_patch(oct)

        plt.show()  # Отображаем график

    def __del__(self):  # Деструктор (вызывается при удалении объекта)
        print('Октагон стерт')
