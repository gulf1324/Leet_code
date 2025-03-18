###########################################################
# not safe if nums is empty
# e.g.) Constraints: "nums is non-empty array"
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = nums[0]
        for i in nums[1:]:
            ans ^= i
        return ans
###########################################################    
# more readable
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
###########################################################    
s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))