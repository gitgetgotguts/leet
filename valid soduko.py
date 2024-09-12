import numpy as np
from collections import Counter


def Valid_Soduko_Square(a, x, y):
    s = set()
    k = len(s)
    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            if a[i][j] == '.':
                continue
            else:
                s.add(a[i][j])
                if len(s) > k:
                    k += 1
                else:
                    return False
    return True


def check_lines(L):
    D = set()
    for i in L:
        j = Counter(i)
        if '.' in j:
            j.pop('.')
        for k in j.values():
            if any(v > 1 for v in j.values()):
                return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        board = np.array(board)
        T = np.transpose(board)
        a = check_lines(T)
        b = check_lines(board)
        c = 1
        for i in range(3):
            for j in range(3):
                c = c and Valid_Soduko_Square(board, i, j)

        return a and b and c


# returning false in the second function wont break from the main one
# solved had to add return True at the end to use binary logic