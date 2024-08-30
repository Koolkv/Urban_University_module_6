class Animal:
    hunger = 'Я бы поел(а)'
    full = 'Я сыт, и мне трудно шевелиться'


    def __init__(self, animal_name, alive=True, fed=False):
        self.name = animal_name
        self.alive = alive
        self.fed = fed

    def __str__(self):
        if self.alive:
            return f'{self.name}'
        else:
            return f'Это был(а) {self.name}.'

    def say(self):
        if self.fed:
            return f' - {self.full}, - сказал(а) {self.name}'
        else:
            return f' - {self.hunger}, - сказал(а) {self.name}'

    def eat(self, food):
        self.food = food
        if self.fed == False:
            if food.edible == False:
                self.alive = False
                self.fed = True
                print(f'{self.name} зажевал(а) {self.food}')
                return self.alive
            else:
                self.fed = True
                print(f'{self.name} зажевал(а) {self.food}')

        else:
            print(self.say())


class Plant:
    edible = False

    def __init__(self, plant_name):
        self.name = plant_name
        # съедобный

    def __str__(self):
        return f'{self.name}'

    def say(self):
        if self.edible == False:
            return f' - Меня не едят, - сказал(а) {self.name}'
        else:
            return f' - Меня можно схрумкать, - сказал(а) {self.name}'


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


wolf = Predator('Серей волк')
cow = Mammal('Корова')
perry = Fruit('Груша')
rose = Flower('Колючая Роза')

print(wolf)
print(wolf.say())

print(cow)
print(cow.say())

print(perry)
print(perry.say())

print(rose)
print(rose.say())

wolf.eat(rose)
print(wolf.fed)
print(wolf.alive)
print(wolf)

cow.eat(perry)
print(cow.fed)
print(cow.alive)
cow.eat(perry)

