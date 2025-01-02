# [0,1,0,3,12]
# >>> [1,3,12,0,0]
#####################################################################################
#
class Solution:
	def moveZeroes(self, nums: list[int]) -> None:
		# Position of last non-zero element placed
		last_non_zero = 0
		
		# Move through array, swapping when we find non-zero elements
		for i in range(len(nums)):
			if nums[i] != 0:
				# Swap current non-zero element with position of last_non_zero
				nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
				last_non_zero += 1
#####################################################################################
# remove zeros as counting(not using pointer), and append whole later
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros = 0
        while 0 in nums:
            nums.remove(0)
            num_zeros += 1
        
        for _ in range(num_zeros):
            nums.append(0)
#####################################################################################

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))