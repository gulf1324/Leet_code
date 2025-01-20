class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pairs = []
        potion_sorted = sorted(potions)
        for spell in spells:
            potion_left, potion_right = 0, len(potions) -1
            while potion_left <= potion_right:
                mid = (potion_left + potion_right) // 2
                if spell * potion_sorted[mid] < success:
                    potion_left = mid + 1
                else:
                    potion_right = mid -1
            ########################################
            pairs.append(len(potions)-potion_left) #
            ########################################
        return pairs
######################################################################################################
# using bisect module
import bisect
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            if spell == 0:
                result.append(0)
                continue

            minimum = (success + spell - 1) // spell # to be exact    ex) minimum = 3
            # minimum = success/spell                # doesn't matter ex) minimum = 2.3333...
            """
            bisect_left returns the index of the first element in 
            p1 that is greater than or equal to p2, 
            so doesn't matter what is used between the two
            """

            index = bisect.bisect_left(potions, minimum)

            result.append(m - index)
        return result
    
s = Solution()
print(s.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
# >> [4,0,3]