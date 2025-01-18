########################################################################
from collections import Counter
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        res = 0
        count = Counter(nums)
        for num in count:
            complement = k - num
            if complement in count:
                if num == complement: 
                    res += count[num] // 2
                else:
                    ###########################################
                    res += min(count[num], count[complement]) #
                    ###########################################
        return res//2
########################################################################
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        #############
        nums.sort() #
        #############
        
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                operations += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1

        return operations
########################################################################

# NOTE:
# 1st attempt -> two pointers, failed because couldn't think of sort() and thought it would be O(n*n)

# * Use Counter when dealing with large, unsorted data.
# * Use two-pointer when memory is tight or the data is already sorted.


s = Solution()
print(s.maxOperations([1,2,3,4], 5)) # >>> 2
print(s.maxOperations([3,1,3,4,3], 6)) # >>> 1