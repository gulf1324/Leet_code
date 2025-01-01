#[1,2,3,4,5] -> True
#[5,4,3,2,1] -> False
#[2,1,5,0,4,6] -> True
#[20,100,10,12,5,13] -> True 
#[2,4,-2,-3] -> False
#[5,1,6] -> False
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        first = float('inf')  
        second = float('inf') 
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True       
        return False
            
s = Solution()
print(s.increasingTriplet([20,100,10,12,5,13]))
