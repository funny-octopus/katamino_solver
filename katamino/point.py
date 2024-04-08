

class Point:
    """Координаты точки"""

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move_x(self, x: int):
        """Сместить точки по оси x на смещение
        :param x: смещение
        """
        self.x += x

    def move_y(self, y: int):
        """Сместить точки по оси x на смещение
        :param y: смещение
        """
        self.y += y

    def move(self, x: int, y: int):
        """Смещение точки по обоим осям
        :param x: смещение по оси x
        :param y: смещение по оси y
        """
        self.move_x(x)
        self.move_y(y)

    def __eq__(self, value: 'Point'):
        """Сравнение на равенство"""
        return all(((self.x == value.x), (self.y == value.y)))

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return f"<{self.x}, {self.y}>"
