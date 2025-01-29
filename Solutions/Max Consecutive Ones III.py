class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start, max_length, zero_count = 0, 0, 0
        
        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            
            # The moment when zero_count > k, window shrinks from start
            while zero_count > k: 
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            
            # max() 1.every for loop / 2.when that happened
            max_length = max(max_length, end - start + 1)
        
        return max_length
    
s = Solution()
print(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
