class Human:

    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.house = House()

    def eating(self):
        self.hunger += 10
        self.house.fridge.food -= 10

    def work(self):
        self.hunger -= 10
        self.house.table.money += 10

    def play(self):
        self.hunger -= 10

    def walk(self):
        self.house.fridge.food += 10
        self.house.table.money -= 10


class House:

    def __init__(self):
        self.fridge = Fridge()
        self.table = Table()


class Fridge:

    def __init__(self):
        self.food = 50


class Table:

    def __init__(self):
        self.money = 0
