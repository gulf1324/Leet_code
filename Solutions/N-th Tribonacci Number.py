#########################################################################################################
# memoization => @lru_cache decorator
from functools import lru_cache
class Solution:
    @lru_cache
    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1) 
#########################################################################################################
# dict memoization
# => computing values top-down as needed(recursive).
# => "memo[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)"
class Solution2:
    def tribonacci(self, n: int) -> int:
        memo = {}

        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)
            return memo[i]
        
        return dp(n)
#########################################################################################################  
# list memoization  
# => building the sequence bottom-up(iterative)
# => "for i in range(1, n+1)"
# best so far
class Solution3:
    def tribonacci(self, n: int) -> int:
        memo=[0]
        for i in range(1, n+1):
            if i<3:
                memo.append(1)
            else:
                # print(i,memo)
                memo.append(memo[i-1]+memo[i-2]+memo[i-3])
        return memo[-1]  
#########################################################################################################  
"""
Tribonacci problem => memoization to avoid redundant calculations. 

Two approaches 
1. Recursive Dictionary Memoization: Uses a dictionary (memo) with a recursive helper function,
                                     time comp : O(n)
                                     space comp : O(n) (+ stack calls)
                                     Lookups require hashing keys, adding overhead.

2. Iterative List Memoization: Builds the sequence in a list (memo) iteratively,
                               time comp : O(n)
                               space comp : O(n)
                               use direct array indexing—fast(hash-free).
"""
s = Solution()
s2 = Solution2()
print(s.fibonacci(6))
# >>> 8

print(s.tribonacci(5))
# >>> 7

print(s.tribonacci(25))
print(s2.tribonacci(25))
# >>> 1389537