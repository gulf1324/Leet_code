class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
###################################################################
s = Solution()
print(s.singleNumber([2,2,1]))
# >>> 1
print(s.singleNumber([4,1,2,1,2]))
# >>> 4 