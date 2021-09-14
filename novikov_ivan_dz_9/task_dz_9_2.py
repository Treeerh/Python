# 2. Реализовать класс Road (дорога).
#
#     определить атрибуты: length (длина), width (ширина);
#     значения атрибутов должны передаваться при создании экземпляра класса;
#     атрибуты сделать защищёнными;
#     определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#     использовать формулу:
#     длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
#     проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width


    def calc(self, kg_layer=25, layer=5):
        work = self.__lenght * self.__width * kg_layer * layer  # self.kg_layer * self.layer
        return f'{self.__lenght} м * {self.__width} м * {kg_layer} кг * {layer} см = {work} кг'


road = Road(15, 45)
print(road.calc())
