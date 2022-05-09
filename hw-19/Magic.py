class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            return 'Шторм'
        if other.name == 'Огонь':
            return 'Пар'
        if other.name == 'Земля':
            return 'Грязь'
        if other.name not in ['Воздух', 'Огонь', 'Земля']:
            return None


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Огонь':
            return 'Молния'
        if other.name == 'Земля':
            return 'Пыль'
        if other.name == 'Вода':
            return 'Шторм'
        if other.name not in ['Вода', 'Огонь', 'Земля']:
            return None


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Земля':
            return 'Лава'
        if other.name == 'Вода':
            return 'Пар'
        if other.name == 'Воздух':
            return 'Молния'
        if other.name not in ['Вода', 'Воздух', 'Земля']:
            return None


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if other.name == 'Огонь':
            return 'Лава'
        if other.name == 'Вода':
            return 'Грязь'
        if other.name == 'Воздух':
            return 'Пыль'
        if other.name not in ['Вода', 'Воздух', 'Огонь']:
            return None
