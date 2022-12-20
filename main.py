class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return float(self.x)

    def get_y(self):
        return float(self.y)

    def get_coords(self):
        return float(self.x), float(self.y)

    def __str__(self):
        return f"{self.name}{self.get_coords()}"

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __eq__(self, other):
        if self.name == other.name and self.get_x() == other.get_x() and\
                self.get_x() == other.get_x():
            return True
        return False

    def __ne__(self, other):
        if ord(self.name) != ord(other.name) and self.get_x() != other.get_x() and \
                self.get_x() != other.get_x():
            return True
        return False

    def __le__(self, other):
        if ord(self.name) <= ord(other.name) and self.get_x() <= other.get_x() and \
                self.get_x() <= other.get_x():
                return True
        return False

    def __lt__(self, other):
        if ord(self.name) < ord(other.name) and self.get_x() < other.get_x() and \
                self.get_x() < other.get_x():
            return True
        return False

    def __ge__(self, other):
        if ord(self.name) >= ord(other.name) and self.get_x() >= other.get_x() and \
                self.get_x() >= other.get_x():
            return True
        return False

    def __gt__(self, other):
        if ord(self.name) > ord(other.name) or self.get_x() > other.get_x() or \
                self.get_x() > other.get_x():
            return True
        return False

p_A1 = Point('A', 1, 2)
p_A2 = Point('A', 2, 1)
p_B1 = Point('B', 2, 3)
p_B2 = Point('B', 2, 3)
print(p_A1 == p_A2, p_B1 == p_B2)
print(p_A1 != p_A2, p_B1 != p_B2)
print(p_A1 < p_A2, p_B1 > p_B2)
print(p_A1 >= p_A2, p_B1 <= p_B2)
print(max(p_A1, p_B2, p_A2, p_B2))
print(min(p_A1, p_B2, p_A2, p_B2))