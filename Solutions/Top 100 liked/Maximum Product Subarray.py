# !!!
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans 
##############################################################################################################################               
s = Solution()
print(s.maxProduct(nums = [2,3,-2,4]))
# >>> 6
print(s.maxProduct(nums = [-2,0,-1]))
# >>> 0
