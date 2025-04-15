# good approach but wrong
# binary search -> all about "left, right, mid" index
# No mid-1, mid +1, etc.
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = min(nums[left], nums[right])
        
        if len(nums) <= 2:
            return minimum
        
        while left < right:
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                right = mid -1
            
            elif nums[mid-1] > nums[mid+1]:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    left = mid +1
                if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                    return nums[mid]
        return minimum
####################################################################################################################################################################################################
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/?envType=study-plan-v2&envId=top-100-liked
class Solution2:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
####################################################################################################################################################################################################
s = Solution()
print(s.findMin([3,4,5,1,2]))
# >>> 1
print(s.findMin([2,1]))
# >>> 1
print(s.findMin([3,1,2]))
# >>> 1
print(s.findMin([2,3,4,5,1]))
# >>> 1
print(s.findMin([2,3,1]))
# >>> 1
print(s.findMin([3,4,5,6,1,2]))
# >>> 1
print(s.findMin([7,8,0,4,5,6]))
# >>> 0