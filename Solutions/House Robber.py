########################################################################
# 1st attempt, not efficient
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        for i in range(2, len(nums)):
            nums[i] += max(nums[:i-1])      # repeated indicing list
        return max(nums[-2], nums[-1])
"""
1st for loop:
nums = [2,1,3,2]
            ^
2nd for loop:
nums = [2,1,3,4]
              ^           
"""
"""
1st for loop:
nums = [1,1,2,1,1,1,1000]
            ^
2nd for loop:
nums = [1,1,2,2,1,1,1000]
              ^
3rd for loop:
nums = [1,1,2,2,3,1,1000]
                ^
4th for loop:
nums = [1,1,2,2,3,3,1000]
                  ^
5th for loop:
nums = [1,1,2,2,3,3,1003]
                      ^
"""
############################################################################################################################
# The most readable, intuitive
# https://leetcode.com/problems/house-robber/solutions/6508823/python-easy-to-understand-detailed-expla-2d2i/
class Solution1:
    def rob(self, nums: list[int]) -> int:
        """
        The process:
        1. Updates the robber's best possible ```total_money``` on the [i]th house.
        2. Checks all houses.
        3. Finally, returns the ```total_money``` the robber has.
        """

        # The robber's initial total_money
        total_money = 0
        
        ########## Base-cases #############
        # No house, no money to steal.
        if not nums: 
            return total_money
        # One house and that's all.
        if len(nums) == 1:
            total_money += nums[0]
            return total_money
        ####################################
        
        # Check first 2 houses
        # update best possible total_money on each house.
        total_money += max(nums[0], nums[1])
        nums[0] = total_money
        nums[1] = total_money
        
        # if only 2 houses, return instantly
        if len(nums) < 3:
            return total_money
        
        # Check the rest
        for i in range(2, len(nums)):
            
            # if current house is worth stealing(== current house's money + 2-houses-back's money > previous house),
            #     total_money is now (current house's money + 2-houses-back's money)
            if nums[i] + nums[i-2] >= nums[i-1]:
                total_money = nums[i] + nums[i-2]
                nums[i] = total_money
            
            # if it's not worth stealing, 
            # the robber doesn't steal from this house,
            # thus same total money as the previouse house
            elif nums[i] + nums[i-2] < nums[i-1]:
                nums[i] = total_money
        
        # return the robber's total_money 
        return total_money
############################################################################################################################
# Slightly optimized
class Solution2:
    def rob(self, nums: list[int]) -> int:
        if not nums: 
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # first 2 houses
        # => in order to decide which house to start
        nums[1] = max(nums[0], nums[1])
        if len(nums) < 3:
            return nums[1]
        
        # the rest
        for i in range(2, len(nums)):
            # compare between
            # 1. current sum (current house + two houses back)
            # => "rob this house plus two back"
            # 2. max so far (previous house)
            # => "skip this house and take the previous max."
            nums[i] = max(nums[i] + nums[i-2], nums[i-1]) 
        
        return nums[-1]
############################################################################################################################    
# The most optimized
class Solution3:
    def rob(self, nums: list[int]) -> int:
        if not nums: 
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # initialize prev1, prev2, 
        prev1 = 0
        prev2 = 0
        
        # then the first 2 for loops naturally negated
        for money in nums:
            current = max(prev2 + money, prev1)
            prev2 = prev1
            prev1 = current
        
        return prev1
########################################################################
s = Solution1()
print(s.rob(nums = [1,2,3,1]))
# >>> 4
print(s.rob(nums = [2,7,9,3,1]))
# # >>> 12
print(s.rob(nums = [2,1,1,2]))
# >>> 4
print(s.rob(nums = [1,1,1,1,1,1,1000]))
# >>> 1003
print(s.rob(nums = [1,1,1,990,1,1,1000]))
# >>> 1991