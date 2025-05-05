class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # left-right flip
        for row in matrix:
            for j in range(len(matrix)//2):
                row[j], row[~j] = row[~j], row[j]
                """
                j == 0 / ~j == -1
                j == 1 / ~j == -2
                j == 2 / ~j == -3
                j == 3 / ~j == -4
                ...
                """
           # == row[j], row[n - 1 - j] = row[n - 1 - j], row[j]
        return matrix
        
########################################################
s = Solution()
print(s.rotate([[1,2,3],
                [4,5,6],
                [7,8,9]]))
# >>> [[7,4,1],
#      [8,5,2],
#      [9,6,3]]