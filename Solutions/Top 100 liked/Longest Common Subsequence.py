class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Extra row and column for empty string cases
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # If characters match, take diagonal value + 1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # If no match, take maximum of left or top value
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])        
        # test
        # import numpy as np
        # import pandas as pd
        # df = pd.DataFrame(np.matrix(dp))
        # df.columns = [i for i in "_" + text2]
        # df.index = [i for i in "_" + text1]
        # print(df,'\n')
        return dp[m][n]
##################################################################################    
s = Solution()
print(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
# >>> 3