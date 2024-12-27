# [1,0,0,0,1], 1 => True
# [1,0,0,0,1], 2 => False
# [1,0,1,0,1], 1 => False
# [1,0,0,1], 1 => False
# [1,0,0,0,0,0,1], 2 => True
# [1,0,0,0,1,0,1], 1 => True
# [1,0,1,0,1,0,1], 1 => False
# [0,0,1,0,1], 1 => True
############################################################################
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i, _ in enumerate(flowerbed):
            if i > 0:
                left = flowerbed[i-1]
            else:
                left = None
            if i == len(flowerbed) -1:
                right = None
            else:
                right = flowerbed[i+1]
            current = flowerbed[i]
            
            if left != 1 and current == 0 and right != 1:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        else:
            return False
############################################################################
# Same logic but better
class Solution2:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        plots = [0] + flowerbed + [0]
        for i in range(1, len(plots) - 1):
            if plots[i-1] == 0 and plots[i] == 0 and plots[i+1] == 0:
                plots[i] = 1
                n -= 1
        return n <= 0
############################################################################   
s = Solution2()
print(s.canPlaceFlowers([1,0,0,0,0,0,1], 2))

