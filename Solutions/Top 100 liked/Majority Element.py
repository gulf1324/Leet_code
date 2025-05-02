class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0 
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
##############################################################################################################################               
s = Solution()
print(s.majorityElement([3,2,3]))
# >>> 3
print(s.majorityElement([3, 3, 4, 2, 3, 5, 3, 6, 7]))