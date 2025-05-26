class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(2)]
        for i in range(1,m):
            for j in range(1,n):
                ############################################
                dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1] #
                ############################################
        return dp[(m-1)&1][-1]
##################################################################################    
s = Solution()
print(s.uniquePaths(m = 3, n = 7))
# >>> 28