# Домашняя работа по уроку "Перегрузка операторов."

# Для решения этой задачи будем пользоваться решением к предыдущей
# задаче "Специальные методы класса".(module_5_2.py)

# Объявление класса House
class House():
    # инициализация характеристик класса House - имя и этажность
    def __init__(self, name, number_of_floors):
        # присвоение self.name значения атрибута name (имя здания)
        self.name = name
        # присвоение self.number_of_floors значения атрибута number_of_floors (этажность здания)
        self.number_of_floors = number_of_floors

    # Создание метода go_to с параметром new_floor и
    # логикой внутри него на основе описания задачи
    # и атрибутом new_floor для "плюшек"
    def go_to(self, new_floor):
        self.new_floor = new_floor
        # Если new_floor больше чем self.number_of_floors или меньше 1,
        # то вывод строки "Такого этажа не существует"
        if int(new_floor) > int(self.number_of_floors) or 1 > int(new_floor):
            print(f'Такого этажа {self.new_floor} не существует в доме "{self.name}"\nВ доме "{self.name}" не более {self.number_of_floors} этажей')
        # вывод на экран (в консоль) значения от 1 до new_floor(включительно)
        else:
            print(f'Этажи в доме "{self.name}":')
            for i in range(int(new_floor)):
                i += 1
                print(i)

    # реализация метода __len__ для возвращения количества этажей здания
    def __len__(self):
        # возвращаем значение количества этажей определенных в методе __init__
        return self.number_of_floors

    # реализация метода __str__ для возвращения строки "Название: <название>,
    # кол-во этажей: <этажи>".
    def __str__(self):
        # возвращаем f строку (форматированная строка, значения в {}
        # принимают ранее присвоенные значения из метода __init__)
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # реализация метода __eq__(self, other). Метод должен возвращать True,
    # если количество этажей одинаковое у self и у other.
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    # реализация метода __lt__(self, other). Метод должен возвращать True,
    # если количество этажей меньше у self чем у other.
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    # реализация метода __le__(self, other). Метод должен возвращать True,
    # если количество этажей меньше или равно у self чем у other.
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    # реализация метода __gt__(self, other). Метод должен возвращать True,
    # если количество этажей больше у self чем у other.
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    # реализация метода __ge__(self, other). Метод должен возвращать True,
    # если количество этажей больше или равно у self чем у other.
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    # реализация метода __ne__(self, other). Метод должен возвращать True,
    # если количество этажей у self не равно other.
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    # реализация метода __add__(self, other). Метод должен возвращать сумму
    # self и other
    def __add__(self, other):
        # проверка на принадлежность other к int или House
        other = other if isinstance(other, int) else other.number_of_floors
        # суммируем number_of_floors и other
        self.number_of_floors += other
        # возвращаем измененный number_of_floors в переменной h_ класса House
        return self

    # реализация метода __iadd__(self, other). Метод должен возвращать сумму
    # self и other
    def __iadd__(self, other):
        # проверка на принадлежность other к int или House
        other = other if isinstance(other, int) else other.number_of_floors
        # суммируем number_of_floors и other
        self.number_of_floors += other
        # возвращаем измененный number_of_floors в переменной h_ класса House
        return self

    # реализация метода __radd__(self, other). Метод должен возвращать сумму
    # self и other
    def __radd__(self, other):
        # проверка на принадлежность other к int или House
        other = other if isinstance(other, int) else other.number_of_floors
        # суммируем number_of_floors и other
        self.number_of_floors = self.number_of_floors + other
        # возвращаем измененный number_of_floors в переменной h_ класса House
        return self

# Исходные данные задачи
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__