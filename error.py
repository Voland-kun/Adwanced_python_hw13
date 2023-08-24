class UserException(Exception):
    pass


class TriangleExistenceError(UserException):
    def __init__(self, *args):
        self.value = args

    def __str__(self):
        return f'Треугольник со сторонами {self.value} не существует.'


class EdgeValueError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'длина стороны треугольника должна быть больше нуля.'


class EdgeTypeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} -> длина стороны треугольника должна быть числом.'


class NotDefinedError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Матрицы {self.value} не совместимы.'


class DifferentSizeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Матрицы {self.value} разного размера.'


class DifferentRowLengthError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} -> строки матрицы разной длины.'


class MatrixTypeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} -> неверный тип данных.'
