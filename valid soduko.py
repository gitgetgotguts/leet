x=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
import numpy as np
from collections import Counter
L=np.transpose(x)


class Solution:
    L=[]
    def isValidSudoku(self, board):
        for i in range(3):
            L.append(board[3*i:(i+1)*3])
            D+str(i)=[]
        for i in range(L):
            for j in range(3):
                D+str(i).append(L[i][j*3,(j+1)*3])
                print(D+str(i))





# D=[]
# for i in L:
#     j=Counter(i)
#     if '.' in j:
#         j.pop('.')
#     D.append(j)
# # for i in D :
# #     if D[i] >1:
# #         print(False)
# #
# ret=[set(i.values()) for i in D]
# print(ret)
# print(L)


