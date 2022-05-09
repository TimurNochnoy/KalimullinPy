class Card:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0


class Black_Jack:
    summa = 0

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def move(self, card_1, card_2):
        if self.summa >= 21:
            card_from_deck_14.value = 1
            self.player_1.points += card_1.value
            self.player_2.points += card_2.value
            print(self.player_1.points, card_1.name)
        else:
            self.player_1.points += card_1.value
            self.player_2.points += card_2.value
            self.summa = self.player_1.points + self.player_2.points
            print(self.player_1.points, card_1.name)

    def win(self):
        if self.player_1.points == self.player_2.points and self.player_1.points <= 21:
            print('Ничья.')
        elif self.player_1.points <= 21 and self.player_2.points > 21:
            print('Победил ' + self.player_1.name + '.')
        elif self.player_1.points <= 21 and self.player_2.points <= 21 and self.player_1.points > self.player_2.points:
            print('Победил ' + self.player_1.name + '.')
        elif self.player_1.points > 21 and self.player_2.points <= 21:
            print('Победил ' + self.player_2.name + '.')
        elif self.player_1.points <= 21 and self.player_2.points <= 21 and self.player_1.points < self.player_2.points:
            print('Победил ' + self.player_2.name + '.')
        else:
            print('Проиграли оба.')
