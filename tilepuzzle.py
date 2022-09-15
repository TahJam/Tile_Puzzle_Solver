# tilepuzzle.py
# Written by Taher Jamali

"""
to run, type 'python3' to command line
\>>> from tilepuzzle import tilepuzzle
\>>> tilepuzzle([[2, 8, 3], [1, 0, 4], [7, 6, 5]], [[1, 2, 3], [8, 0, 4], [7, 6, 5]], 9)
"""


from typing import List
from copy import deepcopy # need this to deep copy lists to functions

visited = dict()


def tilepuzzle(start: List[List[int]], goal: List[List[int]], limit=5):
    return reverse(statesearch([start], goal, [], limit))


def statesearch(unexplored, goal, path, limit):
    if not unexplored or len(path) > limit:  # len(path) > limit will save on recursion calls and allow the program to
        # explore the other branches after the limit has been reached
        return []
    elif goal == head(unexplored):
        return cons(goal, path)
    # check limit and cycles
    elif len(path) > limit and head(unexplored) == path[1]:
        # path has already been explored so program doesn't need to explore it again
        return statesearch(tail(unexplored), goal, path, limit + 1)
    else:
        # print(f'depth is {len(path)} and path is {path}')
        result = statesearch(generateNewStates(head(unexplored)), goal, cons(head(unexplored), path), limit)
        if result:
            return result
        else:
            return statesearch(tail(unexplored), goal, path, limit)



def zeroInTop(matrix: List[List[int]]) -> bool:
    top = matrix[0]
    return True if 0 in top else False


def zeroInBottom(matrix: List[List[int]]) -> bool:
    bottom = matrix[-1]
    return True if 0 in bottom else False


def zeroInRight(matrix: List[List[int]]) -> bool:
    x = len(matrix[0]) - 1
    right = [row[x] for row in matrix]
    return True if 0 in right else False


def zeroInLeft(matrix: List[List[int]]) -> bool:
    x = 0
    left = [row[x] for row in matrix]
    return True if 0 in left else False


def zeroInTopRightCorner(matrix: List[List[int]]):
    return zeroInTop(matrix) and zeroInRight(matrix)


def zeroInTopLeftCorner(matrix: List[List[int]]):
    return zeroInTop(matrix) and zeroInLeft(matrix)


def zeroInBottomRightCorner(matrix: List[List[int]]):
    return zeroInRight(matrix) and zeroInBottom(matrix)


def zeroInBottomLeftCorner(matrix: List[List[int]]):
    return zeroInBottom(matrix) and zeroInLeft(matrix)


# Function that returns index of the element 0 in temp. If no 0 is found, it returns -1,-1
def pos(matrix: List[List[int]]):
    for i, row in enumerate(matrix):
        for j in range(len(row)):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1


def swapBottom(matrix: List[List[int]]) -> List[List[int]]:
    if zeroInBottom(matrix):
        return []
    else:
        temp = deepcopy(matrix)
        row, col = pos(temp)
        swap = row + 1
        temp[row][col], temp[swap][col] = temp[swap][col], temp[row][col]
        return temp


def swapLeft(matrix: List[List[int]]):
    if zeroInLeft(matrix):
        return []
    else:
        temp = deepcopy(matrix)
        row, col = pos(temp)
        swap = col - 1
        temp[row][col], temp[row][swap] = temp[row][swap], temp[row][col]
        return temp


def swapRight(matrix: List[List[int]]):
    if zeroInRight(matrix):
        return []
    else:
        temp = deepcopy(matrix)
        row, col = pos(temp)
        swap = col + 1
        temp[row][col], temp[row][swap] = temp[row][swap], temp[row][col]
        return temp


def swapTop(matrix: List[List[int]]):
    if zeroInTop(matrix):
        return []
    else:
        temp = deepcopy(matrix)
        row, col = pos(temp)
        swap = row - 1
        temp[row][col], temp[swap][col] = temp[swap][col], temp[row][col]
        return temp


def generateNewStates(matrix: List[List[int]]):
    newStates = []
    left = swapLeft(matrix)
    bottom = swapBottom(matrix)
    top = swapTop(matrix)
    right = swapRight(matrix)

    # add to newStates only if the matrix contains something
    if left:
        newStates.append(left)
    if right:
        newStates.append(right)
    if top:
        newStates.append(top)
    if bottom:
        newStates.append(bottom)

    return newStates


# Some simple utility functions to give names to some list operations:
def reverse(st):
    return st[::-1]


def tail(lst):
    return lst[1:]


def head(lst):
    return lst[0]


def cons(item, lst):
    return [item] + lst



