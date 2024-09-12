x=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
import numpy as np
from collections import Counter
L=np.transpose(x)


D=[]
for i in x:
    j=Counter(i)
    if '.' in j:
        j.pop('.')
    D.append(j)

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



