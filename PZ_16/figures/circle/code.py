default_radius: int = 5
pi: float = __import__('math').pi


def circle_perimeter(_r: int = default_radius) -> float:
    """Периметр окружности"""
    return 2 * pi * _r


def circle_area(r_: int = default_radius) -> float:
    """Площадь окружности"""
    return pi * r_ ** 2
