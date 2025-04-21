class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        count = 1
        while count * count <= n:
            sq = count * count
            for i in range(sq, n + 1):
                dp[i] = min(dp[i], dp[i - sq] + 1)
            count += 1
        return dp[n]
#######################################################
s = Solution()
print(s.numSquares(16))
# [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2, 3, 4, 1]
# >>> 1
print(s.numSquares(7))
# [0, 1, 2, 3, 1, 2, 3, 4]
# >>> 4