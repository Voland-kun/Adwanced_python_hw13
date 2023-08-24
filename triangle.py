import error


class ValidateEdge:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not isinstance(value, int | float):
            raise error.EdgeTypeError(value)
        if value <= 0:
            raise error.EdgeValueError(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')


class Triangle:
    a = ValidateEdge()
    b = ValidateEdge()
    c = ValidateEdge()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise error.TriangleExistenceError(self.a, self.b, self.c)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        __p = self.perimeter() / 2
        return (__p * (__p - self.a) * (__p - self.b) * (__p - self.c)) ** 0.5


tr = Triangle(3, 3, 3)
# tr1 = Triangle(3, 3, 7) # TriangleExistenceError
# tr2 = Triangle('o', 3, 4)  # EdgeTypeException
# tr3 = Triangle(-6, 6, 6) # EdgeValueException
