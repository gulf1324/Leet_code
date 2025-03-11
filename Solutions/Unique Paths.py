###########################################################################
# Find pattern -> find general term
class Solution:
    def combination_calc(self, objects : int, sample : int) -> int:
        objects_tmp = objects
        sample_tmp = sample
        for i in range(1, sample):
            objects *= (objects_tmp -i)
            sample *= (sample_tmp-i)
        return int(objects/sample)

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        if m == 2:
            return n
        upper = n + m -2
        bottom = m -1
        return self.combination_calc(upper, bottom)
###########################################################################
# dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        if m == 2:
            return n
        
        # m x n grid
        grid = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]
###########################################################################
# optimized dp => using only two alternating rows
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(2)]
        for i in range(1,m):
            for j in range(1,n):
                ############################################
                dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1] #
                ############################################
        return dp[(m-1)&1][-1]
"""
When performing i & 1, only the last bit (Least Significant Bit, LSB) of i is checked:
-> all even number in bit has 0 at the last bit 

for i in range(5):
    print(i, i&1)
>>> 0 0
>>> 1 1 
>>> 2 0
>>> 3 1
>>> 4 0
"""
###########################################################################    
s = Solution()
print(s.uniquePaths(m=1, n=4))
print(s.uniquePaths(m=4, n=7))