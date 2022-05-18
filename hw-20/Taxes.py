class Property:

    def __init__(self, worth):
        self.worth = worth


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculation(self):
        return self.worth / 1000


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculation(self):
        return self.worth / 200


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculation(self):
        return self.worth / 500
