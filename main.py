from octagon import Octagon  # Импортируем класс Octagon из модуля octagon

def main():  # Создаем функцию main
    oct = Octagon(13)  # Создаем oct
    oct.square()  # Площадь октагона
    oct.perimeter()  # Периметр октагона
    oct.circumcircle()  # Радиус и площадь описанной окружности
    oct.inscribedcircle()  # Радиус и площадь вписанной окружности
    oct.graph()  # Строим график

if __name__ == '__main__':
    main()