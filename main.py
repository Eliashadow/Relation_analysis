"""
Discrete math lab work 1
Relation theory
"""

import math

# def reading(path: str) -> list[list]:
#     '''відкриває і читає файл'''
#     pass

# def writing_in_file(path):
#     '''записує відношення у файл'''
#     pass

# def reflexive_matrix(matrix: list[list]) -> list[list]:
#     '''знаходить рефлексивне замикання'''
#     pass

# def symmetric_matrix(matrix:  list[list]) -> list[list]:
#     '''знаходить рефлексивне замикання'''
#     pass


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
    # matrix_eqv = [row[:] for row in matrix]
    # matrix_eqv = symmetric_matrix(matrix_eqv)
    # matrix_eqv = transition_matrix(matrix_eqv)
    # matrix_eqv = reflexive_matrix(matrix_eqv)

    n = len(matrix)
    quotient_set = []
    # set is like list but more math-like(unorderded, without repetiton)
    visited = set()

    for i in range(n):
        if i not in visited:
            eq_class = [j for j in range(n) if matrix[i][j] == 1]
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


def calculate_num_tras(n: int) -> int:
    '''
    Returns the number of transitive binary relations on a set of n elements.
    n is no bigger than 6
    Sequence values correspond to OEIS A006905.

    :param n: int, A number of element in set matrix 
    :return: int, A number of transitive binary relations.
    If n is bigger than 6, then None

    >>> calculate_num_tras(3)
    171
    >>> calculate_num_tras(7)
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


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())


    # # Showcase for transitive closure
    # matrix_t = transition_matrix(matrix)
    # print(matrix_t)

    # # Showcase for checking if transitive
    # if_transitive(matrix_t)

    # #Showcase for dividing into classes
    # class_eqv(matrix)

    #Showcase for calculating number of transitive connections
    calculate_num_tras(6)
