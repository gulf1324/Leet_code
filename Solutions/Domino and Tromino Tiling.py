##################################################################
# Hard
# top-voted explanation:
# https://leetcode.com/problems/domino-and-tromino-tiling/solutions/6172161/intuitive-approach-using-3-dp-arrays/?envType=study-plan-v2&envId=leetcode-75

# youtube:
# https://www.youtube.com/watch?v=CecjOo4Zo-g (7:45 ~ 16:00)
class Solution1:
    def numTilings(self, n: int) -> int:
        # note: F = Full, T = TopMissing, B = BottomMissing

        F = {0: 1, 1: 1}
        T = {1: 0}
        B = {1: 0}

        for i in range(2, n + 1): 
            F[i] = F[i - 1] + F[i - 2] + T[i - 1] + B[i - 1]
            T[i] = F[i - 2] + B[i - 1]
            B[i] = F[i - 2] + T[i - 1]

        return F[n] % (10 ** 9 + 7)
##################################################################    
# No memoization(optimization, less readable)
class Solution2:
    def numTilings(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        full_prev2 = 1
        full_prev1 = 1
        topMissing_prev1 = 0
        bottomMissing_prev1 = 0
        
        for _ in range(2, n+1):
            current = full_prev1 + full_prev2 + topMissing_prev1 + bottomMissing_prev1
            topMissing_current = full_prev2 + bottomMissing_prev1
            bottomMissing_current = full_prev2 + topMissing_prev1
            
            full_prev2 = full_prev1
            full_prev1 = current
            topMissing_prev1 = topMissing_current
            bottomMissing_prev1 = bottomMissing_current

        return current % (10 ** 9 + 7)
##################################################################
s = Solution2()
print(s.numTilings(2))
# >>> 2
print(s.numTilings(3))
# >>> 5
print(s.numTilings(4))
# >>> 11