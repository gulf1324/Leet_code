########################################################
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path+[s[:i]])
        
        dfs(s, [])
        return res
########################################################
s = Solution()
print(s.partition(s = "aab"))
# >>> [["a","a","b"],["aa","b"]]