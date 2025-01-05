# nums = [1, 12, -5, -6, 50, 3], k = 4
# >>> (12 - 5 - 6 + 50) / 4
# >>> 12.75000
# nums = [-1], k = 1
# [8,0,1,7,8,6,5,5,6,7], 5
####################################################################
# Time limit exceeded
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sums = []
        res = -float("inf")
        for i in range(len(nums)-k+1):
            sums = nums[i:i+k]
            if res < sum(sums)/k:
                res = sum(sums)/k
        return res
####################################################################
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            # print(f"index {i}: {nums[i]} \nindex {i-k}: {nums[i - k]}\n-----------------------")
            
            ###### ★Sliding Window★ #####
            current_sum += nums[i] - nums[i - k]
            ###### ★Sliding Window★ #####
            
            max_sum = max(max_sum, current_sum)

        return max_sum/k

### ★Sliding Window★ #####
##  window += nums[i]   ###
##  window -= nums[i-k] ###
## #★Sliding Window★ #####
    

s = Solution()
print(s.findMaxAverage([8,0,1,7,8,6,5,5,6,7], 5))