from typing import List
from .figure import Figure


class Field:
    """Поле"""

    width: int
    height: int
    figures: List[Figure] = []

    def __init__(self, width: int, height: int = 5):
        if (width * height) % 5 == 0:
            self.width = width
            self.height = height
        else:
            raise ValueError("Неверно заданы значения ширины и высоты для поля")

    def clear(self):
        """Получение стандартных полей"""
        self.figures = []

    def add_figure(self, figure: Figure):
        """Добавить фигуру на поле"""
        self.figures.append(figure)

    def remove_figure(self, figure: Figure):
        if figure in self.figures:
            self.figures.pop(self.figures.index(figure))

    def check_figure_in_field_x(self, figure: Figure) -> bool:
        """Проверка на выход за границы поля"""

        for figure_point in figure.points:
            if figure_point.x > self.width:
                return False
        return True

    def check_figure_in_field_y(self, figure: Figure) -> bool:
        """Проверка на выход за границы поля"""

        for figure_point in figure.points:
            if figure_point.y > self.height:
                return False
        return True

    def check_figures_not_cross(self, figure: Figure) -> bool:
        """Проверка на наложение фигур"""

        for figure_field in self.figures:
            if figure is figure_field:
                continue
            for figure_point in figure.points:
                for figure_field_point in figure_field.points:
                    if figure_point == figure_field_point:
                        return False
        return True

    def print_field(self):
        """Представление в виде текста"""
        lines = [['.' for _ in range(self.width)] for _ in range(self.height)]

        for figure in self.figures:
            for figure_point in figure.points:
                # lines[figure_point.y - 1][figure_point.x - 1] = f"{figure.color}{figure.code_name}"
                lines[figure_point.y - 1][figure_point.x - 1] = f"{figure.color}\u25A0"

        for line in lines:
            for char in line:
                print(char + '  ', end='')
            print('\n', end='')
        print('')

    def __str__(self):
        return f"<Field {self.width}, {self.height}>"

    def __repr__(self):
        return f"<Field {self.width}, {self.height}>"
