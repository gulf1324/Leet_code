############################################################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return nums.index(max(nums))
        left, right = 0, len(nums) -1 
        peak_height = float("-inf")
        nums_sorted = sorted(nums)
        while left <= right:
            mid = (left+right)//2
            if peak_height <= nums_sorted[mid]:
                peak_height = nums_sorted[mid]
                left = mid + 1
            else:
                right = mid -1
        return nums.index(peak_height)
############################################################    
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # approach 1: binary search template II
        left, right = 0, len(nums)-1
        while left < right:
            ################################
            mid = left + (right-left) // 2 #
            ################################
            # only look at the right
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
############################################################

s = Solution()
# print(s.findPeakElement([1,2,1,3,5,6,4]))
# print(s.findPeakElement([1,2]))
# print(s.findPeakElement([1]))
# print(s.findPeakElement([1,2,3]))
print(s.findPeakElement([1,2,3,4,3]))