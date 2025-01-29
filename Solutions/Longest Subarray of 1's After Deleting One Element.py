########################################################
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        start, max_len, zero_count = 0,0,0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count +=1
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -=1
                start +=1
            max_len = max(max_len, i - start)

        return max_len
########################################################
# HOW
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = 0
        count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            ############### ??
            if count > 1: #
            ###############
                if nums[l] == 0:
                    count -= 1
                l += 1
        
        ########################## ??
        return len(nums) - l - 1 # 
        ########################## 
########################################################

s = Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
# >>> 5
print(s.longestSubarray([0,1,1,1,0,1,1,1,1]))