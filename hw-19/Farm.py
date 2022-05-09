class Gardener:

    def __init__(self, name, garden_bed):
        self.name = name
        self.garden_bed = garden_bed

    def care(self):
        return self.garden_bed.grow()

    def harvest(self):
        return self.garden_bed.harvest()


class Potato:

    def __init__(self, number, maturity):
        self.number = number
        self.maturity = maturity

    def info(self):
        return self.maturity

    def grow(self):
        self.maturity += 1


class Garden_bed:

    def __init__(self, potato_list):
        self.potato_list = potato_list

    def info(self):
        return [potato.maturity for potato in self.potato_list]

    def grow(self):
        return [potato.grow() for potato in self.potato_list]

    def harvest(self):
        self.potato_list = []
