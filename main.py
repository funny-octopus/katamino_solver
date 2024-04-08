import os
from katamino import *
from multiprocessing import Process


def move_figures(*figures: Figure, field_: Field):

    for figure in figures:
        field_.add_figure(figure)

        for y in range(field_.height):
            figure.move(x=0, y=y)
            if not field_.check_figure_in_field_y(figure) or not field_.check_figure_in_field_x(figure):
                figure.to_begin()
                field_.remove_figure(figure)
                return
            for _ in range(field_.width):
                if field_.check_figures_not_cross(figure):
                    if len(figures) > 1:
                        gen = move_figures(*figures[1:], field_=field_)
                        for _ in gen:
                            yield
                    else:
                        yield
                figure.move(x=1, y=0)
                if not field_.check_figure_in_field_x(figure):
                    figure.to_begin()
                    break


def rotate_figures(*figures: Figure, first_figure: bool = False):
    if len(figures) > 1:
        gen = rotate_figures(*figures[1:])
        for res in gen:
            a = [figures[0]]
            a.extend(res)
            yield a
    else:
        yield [figures[0]]

    if not first_figure:
        for _ in range(figures[0].rotate_number):
            figures[0].rotate_forward_clock()
            if len(figures) > 1:
                gen = rotate_figures(*figures[1:])
                for res in gen:
                    a = [figures[0]]
                    a.extend(res)
                    yield a
            else:
                yield [figures[0]]
        figures[0].to_default()

        if figures[0].is_mirror and not first_figure:
            figures[0].mirror_x()
            if len(figures) > 1:
                gen = rotate_figures(*figures[1:])
                for res in gen:
                    a = [figures[0]]
                    a.extend(res)
                    yield a
            else:
                yield [figures[0]]

            for _ in range(figures[0].rotate_number):
                figures[0].rotate_forward_clock()
                if len(figures) > 1:
                    gen = rotate_figures(*figures[1:])
                    for res in gen:
                        a = [figures[0]]
                        a.extend(res)
                        yield a
                else:
                    yield [figures[0]]
            figures[0].to_default()


def aaa(*figures: Figure, field_: Field):
    print(os.getpid())
    rf = rotate_figures(*figures, first_figure=True)
    for pos in rf:
        mmm = move_figures(*pos, field_=field_)
        for _ in mmm:
            print(pos)
            field_.print_field()


if __name__ == '__main__':
    input_str = input("Введите номера фигур через пробел: ")
    input_list = input_str.split(' ')
    field_size = len(input_list)

    input_figures_1 = list(map(lambda x: figures_number[x](), map(lambda x: int(x), input_list)))
    p1 = Process(target=aaa, args=(*input_figures_1,), kwargs={'field_': Field(field_size)})

    input_figures_2 = list(map(lambda x: figures_number[x](), map(lambda x: int(x), input_list)))
    input_figures_2[0].rotate_forward_clock()
    p2 = Process(target=aaa, args=(*input_figures_2,), kwargs={'field_': Field(field_size)})

    p1.start()
    p2.start()
