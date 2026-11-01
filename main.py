"""
Discrete math lab work 1
Relation theory
"""

import math
import itertools

def reading(path: str) -> list[list]:
    '''відкриває і читає файл'''

    with open(path, 'r', encoding='utf-8') as file:
        return[[int(x) for x in line.strip()] for line in file]


def writing_in_file(path: str, matrix: list[list]) -> None:
    '''записує матрицю у файл'''

    n = len(matrix)

    with open(path, 'w', encoding='utf-8') as file:
        for row in range(n):
            line = ''.join(map(str,matrix[row]))
            file.write(line + '\n')


def reflexive_matrix(matrix: list[list]) -> list[list]:
    '''знаходить рефлексивне замикання'''

    n = len(matrix)

    for row in range(n):
        for col in range(n):
            if row == col:
                matrix[row][col] = 1
    return matrix


def symmetric_matrix(matrix: list[list]) -> list[list]:
    '''знаходить симетричне замикання'''

    n = len(matrix)

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 1:
                matrix[col][row] = 1
    return matrix


def transition_matrix(matrix: list[list[int]]) -> list[list[int]]:
    '''
    Finds transition closure of binary relation

    :param matrix: list[list[int]], A binary matrix of some relation
    :return: list[list[int]], A binary matrix of transition closure

    >>> matrix = [[0, 1, 0], [1, 1, 1], [0, 0, 0]]
    >>> transition_matrix(matrix)
    [[1, 1, 1], [1, 1, 1], [0, 0, 0]]
    '''

    # Avoiding changing original matrix
    closure = [row[:] for row in matrix]

    # We can find closure only for binary relations so rows == cols
    n = len(matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure


def class_eqv(matrix: list[list[int]]) -> list[list[int]]:
    """
    Making relation into relation of equivalance and then dividing it into classes

    :param matrix: list[list[int]], A binary matrix of some relation
    :return: list[list[int]], A quotient set of relation

    >>> matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    >>> class_eqv(matrix)
    [[0, 1], [2]]
    """

    # Making relation of equivalance by 'str'
    matrix_s = symmetric_matrix(matrix)
    matrix_st = transition_matrix(matrix_s)
    matrix_str = reflexive_matrix(matrix_st)

    n = len(matrix)
    quotient_set = []

    visited = set()

    for i in range(n):
        if i not in visited:
            eq_class = [j for j in range(n) if matrix_str[i][j] == 1]
            quotient_set.append(eq_class)
            visited.update(eq_class)

    return quotient_set


def if_transitive(matrix: list[list[int]]) -> bool:
    '''
    Checks if relation is transitive

    :param matrix: list[list[int]], A binary matrix of some relation
    :return: bool, An answer if relation transitive

    >>> matrix = [[1, 1, 1], [1, 1, 1], [0, 0, 0]]
    >>> if_transitive(matrix)
    True
    >>> matrix = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    >>> if_transitive(matrix)
    False
    '''

    n = len(matrix)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][k] and matrix[k][j] and not matrix[i][j]:
                    return False

    return True


def stirling2(n:int, k: int) -> int:
    """
    Computes the Stirling number of the second kind S(n, k).

    :param n: int, A diffrence between сardinality of set and inner sum counter 
    :param k: int, A diffrence beteem outer sum counter and inner sum counter
    :return: int, The Stirling number of the second kind
    """

    if k < 0 or k > n:
        return 0

    if k == 0:
        return 1 if n == 0 else 0

    stirling_sum = 0
    for j in range(k + 1):
        stirling_sum += (-1)**(k - j) * math.comb(k, j) * (j**n)

    return stirling_sum // math.factorial(k)


def calculate_num_tras_formula(n: int) -> int:
    '''
    Better way
    Returns the number of transitive binary relations on a set of n elements.
    n is no bigger than 6
    Sequence values correspond to OEIS A006905.

    :param n: int, A number of element in set matrix 
    :return: int, A number of transitive binary relations.
    If n is bigger than 6, then None

    >>> calculate_num_tras_formula(3)
    171
    >>> calculate_num_tras_formula(6)
    9415189
    >>> calculate_num_tras_formula(7)
    '''

    if 0 > n or n > 6:
        return None

    p = [1, 1, 3, 19, 219, 4231, 130023]

    total = 0
    for k in range(n + 1):
        inner_sum = 0
        for s in range(k + 1):
            inner_sum += math.comb(n, s) * stirling2(n - s, k - s)

        total += inner_sum * p[k]

    return total


def generate_matrix_combinations(n: int) -> list[list[list[int]]]:
    '''
    Support function for calculate_num_tras
    Returns all possible matrixes of set with n elements
    :param n: int, A number of element in a set
    :return: list[list[list[int]], A list with matrixes represented by lists

    >>> len(generate_matrix_combinations(2))
    16
    '''
    return [[list(prod[i * n:(i + 1) * n]) for i in range(n)]
        for prod in itertools.product([0, 1], repeat=n * n)]


def calculate_num_tras(n: int) -> int:
    '''
    Returns the number of transitive binary relations on a set of n elements.
    n is no bigger than 6.

    :param n: int, A number of element in set  
    :return: int, A number of transitive binary relations.
    If n is bigger than 6, then None

    >>> calculate_num_tras(3)
    171
    >>> calculate_num_tras(7)
    '''

    if 0 > n or n > 6:
        return None

    combinations = generate_matrix_combinations(n)

    num_tras = 0
    for combination in combinations:
        if if_transitive(combination):
            num_tras += 1

    return num_tras


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

    print('==== Writing matrix ====')
    example = [[1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 0]]
    writing_in_file('example.csv', example)

    print('==== Reading matrix from example ====')
    example = reading('example.csv')
    print(example)

    print('==== Making reflexive closure for matrix ====')
    print(reflexive_matrix(example))

    print('==== Making symmetric closure for matrix ====')
    print(symmetric_matrix(example))

    print('==== Making transitive closure for matrix ====')
    print(transition_matrix(example))

    print('==== Checking if matrix transitive ====')
    print(if_transitive(example))

    print('==== Dividing matrix into eqv classes ====')
    print(class_eqv(example))

    print('==== Calculating number of transitive connections ====')
    print(calculate_num_tras_formula(6))

