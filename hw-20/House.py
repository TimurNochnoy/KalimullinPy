class House:

    def __init__(self):
        self.money = 100
        self.food_people = 50
        self.food_cat = 30
        self.dirt = 0


class Husband(House):

    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.status = True
        super().__init__()

    def eat(self):
        pass

    def play(self):
        self.satiety -= 10
        self.happiness += 60

    def work(self):
        self.satiety -= 10
        self.money += 150

    def pet_the_cat(self):
        self.happiness += 5

    def info(self):
        if self.satiety < 0:
            self.status = False
        if self.happiness < 10:
            self.status = False
        return self.status


class Wife(House):

    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.status = True
        super().__init__()

    def eat(self):
        self.satiety += 30
        self.food_people -= 30

    def buy_food(self):
        self.satiety -= 10
        self.food_people += 10
        self.money -= 10
        self.food_cat += 10
        self.money -= 10

    def buy_a_fur_coat(self):
        self.satiety -= 10
        self.money -= 350
        self.happiness += 60

    def clean_up(self):
        self.satiety -= 10
        if self.dirt >= 100:
            self.dirt -= 100
        else:
            self.dirt = 0

    def pet_the_cat(self):
        self.happiness += 5

    def info(self):
        if self.satiety < 0:
            self.status = False
        if self.happiness < 10:
            self.status = False
        return self.status


class Cat(House):

    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.status = True
        super().__init__()

    def eat(self):
        self.satiety += 20
        self.food_people -= 10

    def sleep(self):
        self.satiety -= 10

    def tear_wallpaper(self):
        self.satiety -= 10
        self.dirt += 5

    def info(self):
        if self.satiety < 0:
            self.status = False
        return self.status
