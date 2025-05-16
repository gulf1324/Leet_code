# !!!
class Solution:
    def jump(self, nums:list[int]) -> int:
        n = len(nums)
        if n == 1: 
            return 0
            
        jumps = 0 
        current_max_reach = 0 
        next_max_reach = 0  
        
        for i in range(n - 1):  
            next_max_reach = max(next_max_reach, i + nums[i])
            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach
                
                if current_max_reach >= n - 1:
                    break
        
        return jumps
###################################################################                
s = Solution()
print(s.jump(nums = [2,3,1,1,4]))
# >>> 2
# >>> 2 -> 4
print(s.jump(nums = [2,3,0,1,4]))
# >>> 2
# 2 -> 4
