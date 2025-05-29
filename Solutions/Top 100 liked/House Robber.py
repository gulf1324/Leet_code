class Solution:
    def rob(self, nums: list[int]) -> int:
        # The robber's initial total_money
        total_money = 0
        
        ########## Base-cases #############
        # No house, no money to rob.
        if not nums: 
            return total_money
        # One house and that's all.
        if len(nums) == 1:
            total_money += nums[0]
            return total_money
        ####################################
        
        # Check first 2 houses
        # Update the best possible total_money on the [1]th house
        total_money += max(nums[0], nums[1])
        nums[1] = total_money
        
        # if only 2 houses, return instantly
        if len(nums) < 3:
            return nums[1]
        
        # Check the rest
        for i in range(2, len(nums)):
            
            # if current house is worth robbing
            # (== current house's money + 2-houses-back's money > previous house),
            #     total_money is now (current house's money + 2-houses-back's money)
            if nums[i] + nums[i-2] >= nums[i-1]:
                total_money = nums[i] + nums[i-2]
                nums[i] = total_money
            
            # if it's not worth robbing, 
            # the robber skips this house,
            # thus same total money as the previouse house
            elif nums[i] + nums[i-2] < nums[i-1]:
                nums[i] = total_money
        
        # return the robber's total_money 
        return total_money
###################################################################                
s = Solution()
print(s.rob(nums = [1,2,3,1]))
# >>> 4
print(s.rob(nums = [2,7,9,3,1]))
# >>> 12
