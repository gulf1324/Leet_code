#########################################################################################
# [2,3,5,1,3], 3
# [5,6,8,4,6] 
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        candies_added = [i + extraCandies for i in candies]
        result = []
        greatest_number = True
        
        # 두 개의 전, 후 리스트로 list 하나씩 비교 => O(n^n)
        for after_extra in candies_added:
            for before_extra in candies:
                if after_extra >= before_extra:
                    greatest_number = True
                else:
                    result.append(False)
                    greatest_number = False
                    break
            if greatest_number: 
                result.append(True)
        return result
#########################################################################################
class Solution2:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        old_max = max(candies)
        
        # O(n)
        for candy in candies:
            if candy + extraCandies >= old_max:
                result.append(True)
            else:
                result.append(False)
        return result
#########################################################################################

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))