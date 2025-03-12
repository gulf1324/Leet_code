###############################################################################################################################
# Wrong
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pointer2 = 0
        res = 0
        index = -1
        if len(text1) <= len(text2):
            short = text1
            long = text2
        else:
            short = text2
            long = text1
        for i in range(len(short)):
            while short[i] != long[pointer2] and pointer2 < len(long):
                pointer2 +=1
                if pointer2 > len(long)-1:
                    pointer2 = 0
                    break
            if short[i] == long[pointer2]:
                if pointer2 > index:
                    res += 1
                    index = pointer2
        return res
###############################################################################################################################
# https://leetcode.com/problems/longest-common-subsequence/solutions/6526463/python-seeing-is-worth-thousand-words-ex-chza/
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
###############################################################################################################################    
s = Solution()
# print(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace")) # >>> 3
# print(s.longestCommonSubsequence(text1 = "abc", text2 = "abc"))   # >>> 3
# print(s.longestCommonSubsequence(text1 = "abc", text2 = "def"))   # >>> 0
# print(s.longestCommonSubsequence(text1 = "bl", text2 = "yby"))    # >>> 1
# print(s.longestCommonSubsequence(text1 = "psnw", text2 ="vozsh")) # >>> 1
# print(s.longestCommonSubsequence(text1 ="ezupkr", text2 ="ubmrapg")) # >>> 2
print(s.longestCommonSubsequence(text1 ="oxcpqrsvwf", text2 ="shmtulqrypy")) # >>> 2
"""
   _  s  h  m  t  u  l  q  r  y  p  y
_  0  0  0  0  0  0  0  0  0  0  0  0
o  0  0  0  0  0  0  0  0  0  0  0  0
x  0  0  0  0  0  0  0  0  0  0  0  0
c  0  0  0  0  0  0  0  0  0  0  0  0
p  0  0  0  0  0  0  0  0  0  0  1  1
q  0  0  0  0  0  0  0  1  1  1  1  1
r  0  0  0  0  0  0  0  1  2  2  2  2
s  0  1  1  1  1  1  1  1  2  2  2  2
v  0  1  1  1  1  1  1  1  2  2  2  2
w  0  1  1  1  1  1  1  1  2  2  2  2
f  0  1  1  1  1  1  1  1  2  2  2  2
"""