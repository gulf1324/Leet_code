"""
Levenshtein distance : https://en.wikipedia.org/wiki/Levenshtein_distance#Recursive

1. base case: 
        word1 = "" or word2 = "" => return length of other string
2. recursive case: 
        word1[0] == word2[0] => recurse on word1[1:] and word2[1:]
3. recursive case:
        word1[0] != word2[0] => recurse by inserting, deleting, or replacing
"""
########################################################################################################
# Naive recursive 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)
########################################################################################################
# Memoization
from collections import defaultdict
class Solution:
    def minDistance(self, word1, word2):
        memo = defaultdict(set)
        
        def minDistance2(word1, word2, i, j, memo):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    ans = minDistance2(word1, word2, i + 1, j + 1, memo)
                else: 
                    insert = 1 + minDistance2(word1, word2, i, j + 1, memo)
                    delete = 1 + minDistance2(word1, word2, i + 1, j, memo)
                    replace = 1 + minDistance2(word1, word2, i + 1, j + 1, memo)
                    ans = min(insert, delete, replace)
                memo[(i, j)] = ans
            
            return memo[(i, j)]
        
        return minDistance2(word1, word2, 0, 0, memo)
########################################################################################################
# 2-D DP
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])

        # # test
        # import numpy as np
        # import pandas as pd
        # from tabulate import tabulate
        # df = pd.DataFrame(np.matrix(table))
        # df.columns = [i for i in " " + word2]
        # df.index = [i for i in " " + word1]
        # print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

        return table[-1][-1]
########################################################################################################    
s = Solution()
print(s.minDistance(word1 = "", word2 = "ros"))
print(s.minDistance(word1 = "horse", word2 = "ros"))
# >>> 3 
print(s.minDistance(word1 = "intention", word2 = "execution"))
# >>> 5
print(s.minDistance(word1 = "bcdef", word2 = "abcd"))