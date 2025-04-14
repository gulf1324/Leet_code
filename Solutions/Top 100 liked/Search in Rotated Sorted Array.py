class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
            
            # if right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
################################################################################################
s = Solution()
# print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
# print(s.search(nums = [4,5,6,7,0,1,2], target = 3))
print(s.search(nums = [4,5,6,7,0,1,2], target = 6))
# print(s.search(nums = [7,8,0,1,2,3,4,5,6], target = 6))
# print(s.search(nums = [1], target = 1))
# print(s.search(nums = [1,3], target = 1))