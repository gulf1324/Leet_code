"""
NOTE
Using set/dictionary in Python is using hashmap.
Checking existence using hashmap has O(1) time complexity.
"""
# nums1 = [1,2,3], nums2 = [2,4,6]
# >>> [[1,3],[4,6]]
# nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# >>> [[3],[]]
##########################################################################################
# set(), messy
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = list(set(nums1))
        nums2_set = list(set(nums2))
        for i in nums1:
            if i in nums2_set:
                nums1_set.remove(i)
                nums2_set.remove(i)
        res = [nums1_set, nums2_set]
        return res
##########################################################################################        
# set()
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
##########################################################################################
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        freq_map1 = dict.fromkeys(nums1)  
        freq_map2 = dict.fromkeys(nums2)
        
        # Find unique elements
        result1 = [num for num in freq_map1 if num not in freq_map2]
        result2 = [num for num in freq_map2 if num not in freq_map1]
        
        return [result1, result2]
##########################################################################################

s = Solution()
print(s.findDifference([-3,6,-5,4,5,5], [6,6,-3,-3,3,5]))
# [4, 5, 6, -5, -3] [5, 3, -3, 6]