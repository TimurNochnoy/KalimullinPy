class Parent:

    def __init__(self, name, age, list_of_children):
        self.name = name
        self.age = age
        self.list_of_children = list_of_children

    def information(self):
        return name, age

    def calm_down_the_child(self, child):
        if child.name in self.list_of_children:
            child.calm = 'Спокойный'
        else:
            print('Это не мой ребенок.')

    def feed_the_child(self, child):
        if child.name in self.list_of_children:
            child.hunger = ('Сытый')
        else:
            print('Это не мой ребенок.')


class Child:

    def __init__(self, name, age, calm, hunger):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

    def check(self, parent):
        if self.age + 16 < parent.age:
            print('OK.')
        else:
            print('Возраст должен быть меньше возраста родителя хотя бы на 16 лет.')
