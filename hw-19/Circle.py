class Circle:
    pi = 3.1415926
    def __init__(self, x_coord, y_coord, radius):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius

    def increase(self, coefficient):
        self.radius *= coefficient

    def intersection(self, other):
        if (self.x_coord - other.x_coord) ** 2 + (self.y_coord - other.y_coord) ** 2 <= (
                self.radius + other.radius) ** 2:
            print('Yes')
        else:
            print('No')
