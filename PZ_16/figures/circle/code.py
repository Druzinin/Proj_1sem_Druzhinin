from math import pi
_default_radius = 5


def circle_perimeter(r: int = _default_radius) -> float:
    """Периметр окружности"""
    return 2 * pi * r


def circle_area(r: int = _default_radius) -> float:
    """Площадь окружности"""
    return pi * r ** 2
