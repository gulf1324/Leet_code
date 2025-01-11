####################################################################
import numpy as np
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        grid_T = np.array(grid).T
        grid_dict = {}
        grid_T_dict = {}
        res = 0
        for i in range(len(grid)):
            grid_dict[i] = grid[i]
            grid_T_dict[i] = grid_T[i]
        
        for row in grid_dict:
            for row_T in grid_T_dict:
                if grid_dict[row] == list(grid_T_dict[row_T]):
                    res +=1
        return res
####################################################################
"""
tuple(rows)
>>> This is necessary because lists are mutable 
    and cannot be used as dictionary keys or counted directly with ```Counter```.
    However, Tuples, being immutable, are hashable and can be used as keys.
"""
from collections import Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        res = 0
        
        # duplicated row count
        row_count = Counter(tuple(row) for row in grid)
        # >>> Counter({(3, 2, 1): 1, 
        #              (1, 7, 6): 1, 
        #              (2, 7, 7): 1})
        
        # list(zip(*grid)
        # >>> [(3, 1, 2), 
        #      (2, 7, 7), 
        #      (1, 6, 7)]
        
        for col in zip(*grid):
            res += row_count[tuple(col)]
        return res
####################################################################            
        
        
    
s = Solution()
print(s.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))
        