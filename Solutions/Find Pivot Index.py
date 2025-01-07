# [1,7,3,6,5,6]
# >>> 3
# [2,1,-1]
# >>> 0
########################################################
# 1st attempt (Poor runtime)
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left = []
        sum_right = []
        for i, _ in enumerate(nums):
            sum_left = sum(nums[:i])
            sum_right = sum(nums[i+1:])
            if sum_left == sum_right:
                return i
            else:
                pass
        return -1
########################################################
# 2nd attempt
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left = sum(nums[:0])
        sum_right = sum(nums[1:])
        if sum_left == sum_right:
            return 0
        for i in range(len(nums)-1):
            sum_left += nums[i]
            sum_right -= nums[i+1]
            if sum_left == sum_right:
                return i + 1
            else:
                pass
        return -1
########################################################    
# More efficient
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
########################################################
    
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))