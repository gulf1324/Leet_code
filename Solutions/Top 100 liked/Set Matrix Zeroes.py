"""
Do not return anything, modify matrix in-place instead.
"""
# import numpy as np
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zero_x = set()
        zero_y = set()
        for r_i, r in enumerate(matrix):
            for c_i, value in enumerate(r):
                if value == 0:
                    zero_x.add(r_i)
                    zero_y.add(c_i)
        
        for i in zero_x:
            matrix[i] = [0] * len(matrix[0])
        
        for j in zero_y:
            for row in matrix:
                row[j] = 0

        # using numpy
        # matrix = np.array(matrix)
        # for i in zero_x:
        #     matrix[i,:] = 0
        # for j in zero_y:
        #     matrix[:,j] = 0
        # matrix = matrix.tolist()
##################################################################################    
s = Solution()
print(s.setZeroes(matrix = [[1,1,1],
                            [1,0,1],
                            [1,1,1]]))
# >>> [[1,0,1],
#      [0,0,0],
#      [1,0,1]]]

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
print(s.setZeroes(matrix))
