from .figure import Figure
from .point import Point
from colorama import Fore


class F1(Figure):
    """фигура палка"""

    code_name = "I"
    rotate_number = 1
    is_mirror = False
    color = Fore.BLUE
    default_points = (Point(1, 1), Point(2, 1), Point(3, 1), Point(4, 1), Point(5, 1))


class F2(Figure):
    """фигура Г"""

    code_name = "G"
    color = Fore.LIGHTYELLOW_EX
    default_points = (Point(1, 1), Point(2, 1), Point(1, 2), Point(1, 3), Point(1, 4))


class F3(Figure):
    """фигура i"""

    code_name = "i"
    color = Fore.MAGENTA
    default_points = (Point(1, 1), Point(1, 2), Point(1, 3), Point(1, 4), Point(2, 2))


class F4(Figure):
    """фигура 4"""

    code_name = "4"
    color = Fore.RESET
    default_points = (Point(2, 1), Point(2, 2), Point(1, 2), Point(1, 3), Point(1, 4))


class F5(Figure):
    """фигура уголок"""

    code_name = "L"
    is_mirror = False
    color = Fore.LIGHTBLUE_EX
    default_points = (Point(1, 1), Point(1, 2), Point(1, 3), Point(2, 3), Point(3, 3))


class F6(Figure):
    """фигура 6"""

    code_name = "6"
    color = Fore.LIGHTRED_EX
    default_points = (Point(1, 1), Point(1, 2), Point(1, 3), Point(2, 2), Point(2, 3))


class F7(Figure):
    """фигура C"""

    code_name = "C"
    is_mirror = False
    color = Fore.YELLOW
    default_points = (Point(1, 1), Point(1, 2), Point(2, 2), Point(3, 1), Point(3, 2))


class F8(Figure):
    """фигура Z"""

    code_name = "Z"
    rotate_number = 1
    color = Fore.CYAN
    default_points = (Point(1, 1), Point(2, 1), Point(2, 2), Point(2, 3), Point(3, 3))


class F9(Figure):
    """фигура F"""

    code_name = "F"
    color = Fore.LIGHTBLACK_EX
    default_points = (Point(1, 3), Point(2, 1), Point(2, 2), Point(2, 3), Point(3, 2))


class F10(Figure):
    """фигура T"""

    code_name = "T"
    is_mirror = False
    color = Fore.GREEN
    default_points = (Point(1, 1), Point(2, 1), Point(3, 1), Point(2, 2), Point(2, 3))


class F11(Figure):
    """фигура W"""

    code_name = "W"
    is_mirror = False
    color = Fore.LIGHTGREEN_EX
    default_points = (Point(1, 1), Point(1, 2), Point(2, 2), Point(2, 3), Point(3, 3))


class F12(Figure):
    """фигура X"""

    code_name = "X"
    rotate_number = 0
    is_mirror = False
    color = Fore.RED
    default_points = (Point(1, 2), Point(2, 1), Point(2, 2), Point(2, 3), Point(3, 2))
