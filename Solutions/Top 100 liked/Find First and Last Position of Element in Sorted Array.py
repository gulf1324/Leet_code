# My attempt
# passed but inefficient
# if mid == target, shrinks from left and right by 1 until both are the same.
#                                ^^^^^^^^^^^^^^^^^^^
#                                 inefficient for examples like:
#                                                                nums = [1]*10**6 + [2] *10**6 + [3]*10**6
class Solution1:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1

        while nums[left] != nums[right]:
            mid = (left + right)//2
            if nums[mid] == target:
                if nums[left] == target and target != nums[right]:
                    right -=1
                elif nums[right] == target and target != nums[left]:
                    left +=1
                else:
                    left += 1
                    right -= 1
            if nums[mid] < target:
                left = mid +1
            if nums[mid] > target:
                right = mid -1
        
        return [left, right] if nums[left] == target else [-1,-1]
#################################################################################
# efficient
import bisect
class Solution2:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        # same as bisect_left ==> finds the left-most "insertion point(index)" while maintaining order ==> thus same as first seen element
        # == bisect.bisect_left()
        def find_left():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:  ### -->> if mid == target, right shrinks
                    right = mid - 1
            return left

        # same as bisect_right -1 ==> finds the right-most "insertion point(index)" while maintaining order, thus -1 ==> last seen element
        # == bisect.bisect_right() - 1
        def find_right():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = find_left()
        right_index = find_right()

        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
#################################################################################
# same as solution2
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_index = bisect.bisect_left(nums, target)
        right_index = bisect.bisect_right(nums, target)-1

        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
#################################################################################
# s = Solution1()
s2 = Solution2()
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
# # >>> [3, 4]
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
# >>> [-1, -1]
# print(s.searchRange(nums = [1,2,3], target = 2))
# >>> [1, 1]
# print([1] + [2] * 10**6 + [3])
# print(s.searchRange(nums = [1]*10**6 + [2] *10**6 + [3]*10**6, target=2))
# print(s2.searchRange(nums = [1]*10**6 + [2] *10**6 + [3]*10**6, target=2))
print(s2.searchRange(nums = [5,8,8,8,8,10], target=8))