class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = int(age)


class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        pass


class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        return 13000


class Agent(Employee):

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.sales = int(sales)

    def salary(self):
        return 5000 + self.sales * 0.05


class Worker(Employee):

    def __init__(self, name, surname, age, time):
        super().__init__(name, surname, age)
        self.time = int(time)

    def salary(self):
        return 100 * self.time
