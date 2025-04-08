from bisect import bisect_left 
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return bisect_left(nums, target) 
######################################################################
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        p, q = 0, len(nums)-1
        while p <= q:
            mid = (p + q) // 2
            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    q = mid-1
                else:
                    p = mid+1
        return p
######################################################################    
s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target= 5))
# >>> 2
print(s.searchInsert(nums = [1,3,5,6], target = 2))
# >>> 1
print(s.searchInsert(nums = [1,3,5,6], target = 7))
# >>> 4
print(s.searchInsert(nums = [1,3], target = 2))
# >>> 1