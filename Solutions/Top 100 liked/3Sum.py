# sort, fix i, move p or q 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue          
            
            p = i + 1
            q = len(nums) - 1

            while p < q:
                total = nums[i] + nums[p] + nums[q]
                if total > 0:
                    q -= 1
                elif total < 0:
                    p += 1
                else:
                    res.append([nums[i], nums[p], nums[q]])
                    p += 1
                    while nums[p] == nums[p-1] and p < q:
                        p += 1
        return res
###################################################################                
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
# >>> [[-1,-1,2],[-1,0,1]]
print(s.threeSum([0,0,0,0]))
# >>> [[0,0,0],[0,0,0],[0,0,0]] (x)
# >>> [[0,0,0]] (o)
print(s.threeSum([-1,0,1,0]))
# >>> [[-1,0,1],[-1,1,0]] (x)
# >>> [[-1,0,1]] (o)
print(s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
# >>> [[-4,2,2],[-2,0,2],[-3,1,2]] (x)
# >>> [[-4,2,2],[-2,0,2],[-3,1,2],[-10,5,5],[-5,0,5],[-3,-2,5]] (o)