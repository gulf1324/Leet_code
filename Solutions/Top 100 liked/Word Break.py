class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # no need to check further if dp[i] is True

        return dp[n]
#######################################################
s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
# final dp = [True, F, F, F, True, F, F, F, True]
#             ""            "leet"         "code"
# True
print(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
# False