x=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
import numpy as np
from collections import Counter





def Valid_Soduko_Square(a, x, y):
    s={}
    k=len(s)
    for i in range(x*3, x*3 + 3):
        for j in range(x*3, x*3 + 3):
            if a[i][j] == '.': continue
            else:
                s.append(a[i][j])
                if len(s) > k: k+= 1
                else: return False
    return True

ret=[set(i.values()) for i in D]

def check_lines(L):
    D=set()
    for i in L:
        j=Counter(i)
        if '.' in j:
            j.pop('.')
        D.add([set(i.values()) for i in D])
    if D!={{1}}:
        return False




