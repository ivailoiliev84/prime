input_number = int(input())

sheet = []


def is_prime(num):
    """
    :param num: digit which will be checking
    :return: boolean True or False
    """
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def create_primes():
    """
    :return: list from prime numbers in range from 2 to 100, recommended  value!
    """
    for i in range(2, 100):
        if is_prime(i):
            sheet.append(i)

    return sheet[0: input_number]


def create_matrix(num):
    matrix = []
    for i in range(num):
        matrix.append([])
        for j in range(num):
            matrix[-1].append(".")

    return matrix


matrix = create_matrix(input_number + 1)

"""
create the first cell empty -> like the given example...

[' ', 2, 3, 5, 7, 11]
[2, 4, 6, 10, 14, 22]
[3, 6, 9, 15, 21, 33]
[5, 10, 15, 25, 35, 55]
[7, 14, 21, 35, 49, 77]
[11, 22, 33, 55, 77, 121]

"""

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == 0 and j == 0:
            matrix[i][j] = ' '

prime_seq = create_primes()

"""
filling columns
"""
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j > 0:
            matrix[i][j] = prime_seq[j - 1]

"""
filling rows
"""
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i > 0:
            matrix[i][j] = prime_seq[i - 1]

"""
calculate matrix ciel values
"""

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i > 0 and j > 0:
            matrix[i][j] = int(matrix[i][j]) * int(matrix[i - i][j])

for i in matrix:
    print(i)
