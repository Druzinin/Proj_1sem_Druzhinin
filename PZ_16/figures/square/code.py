a: int = 15


def square_perimeter(_a: int = a) -> int:
    """Периметр квадрата"""
    return _a * 4


def square_area(a_: int = a) -> int:
    """Площадь квадрата"""
    return a_ ** 2
