import numpy as np


class Player:

    def __init__(self, name):
        self.name = name


class Area:

    def __init__(self, degree):
        self.degree = int(degree)
        self.field = np.ones((int(degree), int(degree))) * -1

    def show(self):
        print(' ', end='')
        for i in range(self.degree):
            print(' ' + str(i), end='')
        print()
        for i in range(self.degree):
            s = []
            for j in range(self.degree):
                if self.field[i][j] == -1:
                    s.append(' _')
                if self.field[i][j] == 0:
                    s.append(' 0')
                if self.field[i][j] == 1:
                    s.append(' +')
            print(str(i) + "".join(s))
        print()


class Game:

    def __init__(self, player_1, player_2, cells):
        self.player_1 = player_1
        self.player_2 = player_2
        self.queue = 0
        self.k = -2
        self.area = Area(cells)

    def move(self):
        if self.queue % 2 == 0:
            print('Ходит', self.player_1.name, 'и ставит 0')
        else:
            print('Ходит', self.player_2.name, 'и ставит +')
        self.queue += 1
        sign_str = input('Введите координату и значение: ')
        x = int(sign_str.strip().split()[0])
        y = int(sign_str.strip().split()[1])
        if sign_str.strip().split()[2] == '0':
            self.area.field[x][y] = 0
        if sign_str.strip().split()[2] == '+':
            self.area.field[x][y] = 1
        self.area.show()

    def win(self):
        if self.k == -1 or self.k == -2:
            for i in range(self.area.degree):
                self.k = self.area.field[i][0]
                for j in range(self.area.degree):
                    if self.area.field[i][j] != self.k:
                        self.k = -2
                if self.k == 0:
                    print('Выиграл', self.player_1.name)
                    break
                if self.k == 1:
                    print('Выиграл', self.player_2.name)
                    break
        if self.k == -1 or self.k == -2:
            for j in range(self.area.degree):
                self.k = self.area.field[0][j]
                for i in range(self.area.degree):
                    if self.area.field[i][j] != self.k:
                        self.k = -2
                if self.k == 0:
                    print('Выиграл', self.player_1.name)
                    break
                if self.k == 1:
                    print('Выиграл', self.player_2.name)
                    break
        if self.k == -1 or self.k == -2:
            self.k = self.area.field[0][0]
            for i in range(self.area.degree):
                if self.area.field[i][i] != self.k:
                    self.k = -2
            if self.k == 0:
                print('Выиграл', self.player_1.name)
            if self.k == 1:
                print('Выиграл', self.player_2.name)
        if self.k == -1 or self.k == -2:
            self.k = self.area.field[0][self.area.degree - 1]
            for i in range(self.area.degree):
                if self.area.field[i][self.area.degree - 1 - i] != self.k:
                    self.k = -2
            if self.k == 0:
                print('Выиграл', self.player_1.name)
            if self.k == 1:
                print('Выиграл', self.player_2.name)
