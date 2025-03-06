############################################################################
from functools import lru_cache
# Top-down recursive dp
# Time limit exceeded due to intense recursion call stacks w/o @lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @lru_cache
        def dp(n):  
            # if index is 0 or 1 it means it's a starting point 
            if n < 2: 
                return cost[n] 
            
            # else, it means it needs to search deeper to the starting point
            return cost[n] + min(dp(n-1), dp(n-2))
		
        length = len(cost) 
        # top-down recursion
        return min(dp(length-1), dp(length-2))
############################################################################
# list 'cost' updates every for loop
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(2, len(cost)):
            
            # cost[i] now shows how much cost is needed to reach that index [i]
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])
"""
cost = [10, 15, 20, 25, 30]

1st for loop i == 2:
min(15, 10) == 10, added to cost[2]
   cost = [10, 15, 30, 25, 30]
                   ^^

2nd for loop i == 3:
min(30, 15) == 15, added to cost[3]
   cost = [10, 15, 30, 40, 30]
                       ^^

3rd for loop i == 4:
min(30, 40) == 30, added to cost[4]
   cost = [10, 15, 30, 40, 60]
                           ^^

loop end

return min(60, 40) ==> 40
"""
############################################################################
"""
DP ==> recurrence
cost[i] += min(cost[i-1], cost[i-2]) is a recurrence in disguise: 
it says the cost to reach step i depends on the minimum of the costs to reach the two previous steps, 
plus the cost at [i]. It's a rule that repeats, connecting each step to the ones before it. 
Whether you're coding it recursively or iteratively, 
that recurring pattern is what makes DP tick—turning a messy, exponential problem into something linear by reusing past results.
 - Grok
"""
s = Solution()
# print(s.minCostClimbingStairs(cost = [10,15,20]))
# # >>> 15
# print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
# >>> 6
print(s.minCostClimbingStairs(cost = [10, 15, 20, 25, 30]))
# >>> 40 