class CreatePrime:

    def __init__(self, number):
        self.number = number

    @staticmethod
    def is_prime(num):
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

    def create_primes(self):
        sheet = []
        for i in range(2, 100):
            if self.is_prime(i):
                sheet.append(i)

        return sheet[0: self.number]


class ModerateMatrix:

    def __init__(self, number):
        self.number = number

        """
        Make first cell empty like a given example.
              
           [' ', 2, 3, 5, 7, 11]
           [2, 4, 6, 10, 14, 22]
           [3, 6, 9, 15, 21, 33]
           [5, 10, 15, 25, 35, 55]
           [7, 14, 21, 35, 49, 77]
           [11, 22, 33, 55, 77, 121]
        """

    def make_first_cell_empty(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == 0 and j == 0:
                    matrix[i][j] = ' '
        return matrix


class FillMatrix(CreatePrime, ModerateMatrix):
    """
    Fill the firs row and the first column on the matrix with prime numbers.
    """

    def __init__(self, number):
        super().__init__(number)

    def fill_matrix(self, matrix):
        prime_seq = self.create_primes()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j > 0:
                    matrix[i][j] = prime_seq[j - 1]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i > 0:
                    matrix[i][j] = prime_seq[i - 1]
        return matrix


class CalculateMatrix(FillMatrix):
    """
    Calculate cells values!
    """

    def __init__(self, number):
        super(CalculateMatrix, self).__init__(number)

    def calculate_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i > 0 and j > 0:
                    matrix[i][j] = int(matrix[i][j]) * int(matrix[i - i][j])
        return matrix


class Matrix(CalculateMatrix):

    """
    Main class  create the matrix with given value of N
    """

    def __init__(self, number):
        super(Matrix, self).__init__(number)
        self.number = number
        if self.number < 0:
            raise ValueError("The input must be positive value")
        self.matrix = self.get_matrix(number + 1)

    def get_matrix(self, number):
        matrix = []
        for i in range(number):
            matrix.append([])
            for j in range(number):
                matrix[-1].append(".")

        matrix = self.make_first_cell_empty(matrix)
        matrix = self.fill_matrix(matrix)
        matrix = self.calculate_matrix(matrix)
        return matrix

    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)


m1 = Matrix(5)
print(m1)
