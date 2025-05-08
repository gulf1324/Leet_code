class Solution:
    def moveZeroes(self, nums : list[int]) -> None:
        left = 0
        for i, _ in enumerate(nums):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
###################################################################
class Solution:
    def moveZeroes(self, nums : list[int]) -> None:
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
###################################################################                
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
# >>> [1,3,12,0,0]
print(s.moveZeroes([0]))
# >>> [0]
