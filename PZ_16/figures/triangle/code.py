_a, _b, _c = 7, 2, 8


def triangle_perimeter(a: int = _a,
                       b: int = _b,
                       c: int = _c) -> int:
    """Периметр треугольника"""
    return a + b + c


def triangle_area(a: int = _a,
                  b: int = _b,
                  c: int = _c) -> float:
    """Площадь треугольника"""
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5 if (p := triangle_perimeter(a, b, c) / 2) else 0.0
