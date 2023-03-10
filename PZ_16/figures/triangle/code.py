a: int = 7
b: int = 2
c: int = 8


def triangle_perimeter(_a: int = a,
                       _b: int = b,
                       _c: int = c) -> int:
    """Периметр треугольника"""
    return _a + _b + _c


def triangle_area(a_: int = a,
                  b_: int = b,
                  c_: int = c) -> float:
    """Площадь треугольника"""
    return (p * (p - a_) * (p - b_) * (p - c_)) ** 0.5 if (p := triangle_perimeter(a_, b_, c_) / 2) else 0.0
