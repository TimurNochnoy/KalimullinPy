import math as m


class Automobile:

    def __init__(self, x_coord, y_coord, alpha):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.aplha = alpha

    def move(self, length, phi=0):
        self.x_coord += length * m.cos(self.aplha + phi)
        self.y_coord += length * m.sin(self.aplha + phi)

    def info(self):
        print(self.x_coord, self.y_coord)


class Bus(Automobile):

    def __init__(self, x_coord, y_coord, alpha, passengers):
        super().__init__(x_coord, y_coord, alpha)
        self.passengers = passengers
        self.one_stop_cost = 10
        self.money = 0

    def move(self, length, phi=0):
        self.x_coord += length * m.cos(self.aplha + phi)
        self.y_coord += length * m.sin(self.aplha + phi)
        self.money += self.one_stop_cost * self.passengers

    def info(self):
        print(self.x_coord, self.y_coord, self.money)

    def come_in(self, amount):
        self.passengers += amount

    def get_off(self, amount):
        self.passengers -= amount
