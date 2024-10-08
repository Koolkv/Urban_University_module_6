class Vehicle:
    __COLOR_VARIANTS = ['coSmoS', 'black', 'dark blue', ]

    def __init__(self, owner=str, model=str, engine_power=0, color=str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        set_color = False
        for i in self.__COLOR_VARIANTS:
            if i.lower() == self.new_color.lower():
                set_color = True
                break
        if set_color:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


car_632 = Sedan('KoolikovN', 'MINI', 184, 'brown')
car_632.print_info()
car_632.set_color('Cosmos')
car_632.get_color()
car_632.set_color('piggy pink')
car_632.get_color()
car_632.owner = 'Novikov'
car_632.print_info()
