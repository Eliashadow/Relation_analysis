"""
Discrete math lab work 1
Relation theory
"""

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


def calculate_num_tras(n: int) -> int | None:
    '''
    Returns the number of transitive binary relations on a set of n elements.
    n is no bigger than 6
    Sequence values correspond to OEIS A006905.

    :param n: int, A number of element in set matrix 
    :return: int or None, A number of transitive binary relations.
    If n is bigger than 6, then None

    >>> calculate_num_tras(3)
    171
    >>> calculate_num_tras(7)
    '''

    match n:
        case 0:
            result = 1
        case 1:
            result = 2
        case 2:
            result = 13
        case 3:
            result = 171
        case 4:
            result = 3994
        case 5:
            result = 154303
        case 6:
            result = 9415189
        case _:
            result =  None

    return result


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

    # #Showcase for calculating number of transitive connections
    # calculate_num_tras(6)
