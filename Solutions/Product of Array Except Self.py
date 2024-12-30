###################################################################
# Time limit exceeded
from copy import deepcopy
import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res_list = []
        for i in nums:
            a_copy = deepcopy(nums)
            a_copy.remove(i)
            res_list.append(math.prod(a_copy))
        return res_list
###################################################################
# Time limit exceeded
import math 
class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1]*len(nums)
        for i,_ in enumerate(nums):
            result[i] = (math.prod(nums[:i])*math.prod(nums[i+1:]))
        return result
###################################################################
class Solution3:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n 

        # prefix 
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # backwards suffix 
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

s = Solution3()
print(s.productExceptSelf([1,2,3,4]))
