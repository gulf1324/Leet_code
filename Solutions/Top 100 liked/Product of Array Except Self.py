class Solution:
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
###################################################################                
s = Solution()
print(s.productExceptSelf(nums = [1,2,3,1]))
# >>> 4
print(s.productExceptSelf(nums = [2,7,9,3,1]))
# >>> 12
