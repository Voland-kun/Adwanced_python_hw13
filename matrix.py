import error


class Matrix:
    """"Класс матрицы"""

    def __init__(self, list_of_lists):
        """Создаёт объект класса Matrix принимая список списков, содержащих числа."""
        if not isinstance(list_of_lists, list):
            raise error.MatrixTypeError(list_of_lists)
        self.matrix = []
        length = len(list_of_lists[0])
        count = 0
        for i in list_of_lists:
            if not isinstance(list_of_lists, list):
                raise error.MatrixTypeError(i)
            if len(i) == length:
                self.matrix.append(i.copy())
            else:
                raise error.DifferentRowLengthError(f'{list_of_lists}->{i}')
            for j in i:
                if not isinstance(j, int | float):
                    raise error.MatrixTypeError(j)
            count += 1
            self.rows = count
            self.columns = length

    def __str__(self):
        """Печать матрицы"""
        format_size = []
        for col in zip(*self.matrix):
            col_len = [len(str(x)) for x in col]
            format_size.append(max(col_len))
        res = '\n'
        for i in self.matrix:
            for n, e in enumerate(i):
                res += f'{e:>{format_size[n]}}  '
            res += '\n'
        return res

    def __eq__(self, other):
        """Сравнение матриц."""
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            for i in range(self.columns):
                for j in range(self.rows):
                    if self.matrix[j][i] != other.matrix[j][i]:
                        return False
            return True
        else:
            return False

    def __add__(self, other):
        """Сложение матриц. Для матриц одной размерности"""
        if self.rows == other.rows and self.columns == other.columns:
            sum_res = [list(map(sum, zip(*i))) for i in zip(self.matrix, other.matrix)]
        else:
            raise error.DifferentSizeError(f'{self}и{other}')
        return Matrix(sum_res)

    def __mul__(self, other):
        """Умножение матриц. Для совместимых матриц."""
        if self.rows == other.columns and self.columns == other.rows:
            mul_res = [[sum(a * b for a, b in zip(ra, cb)) for cb in zip(*other.matrix)] for ra in self.matrix]
            return Matrix(mul_res)
        else:
            raise error.NotDefinedError(f'{self}и{other}')


a = [1, 2]
b = [4, 5]
e = [6, 7]
f = [85684, 9, 10]
c = [9, 8, 7]
d = [6, 'a', 4]
r1 = [a, b, e]
r3 = [a, c]
r5 = [c, f, d]

m1 = Matrix(r1)
# m3 = Matrix(r3) # DifferentRowLengthError
# m5 = Matrix(r5) # MatrixTypeError
m6 = Matrix([[1, 2], [4, 5]])

# print(m1 * m6) # NotDefinedError
print(m1 + m6)  # DifferentSizeError

# help(Matrix)
