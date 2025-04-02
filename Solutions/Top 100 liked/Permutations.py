class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = [False] * len(nums)
        
        def backtrack(used : list[bool], combination : list[int]):
            if len(combination) == len(nums):
                res.append(combination[:])
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                
                combination.append(num)
                used[i] = True
                backtrack(used, combination)
                combination.pop()
                used[i] = False
        
        backtrack(used, [])
        return res
################################################################################
s= Solution()
print(s.permute(nums = [1,2,3]))
# >>> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]