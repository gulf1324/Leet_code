# Memory limit exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        
        def backtrack(steps:list[int], total_steps:int) -> list[int]:
            if total_steps == n:
                res.append(steps[:])
                return
            if total_steps > n:
                return

            for i in [1, 2]:
                steps.append(i)
                total_steps += i
                backtrack(steps, total_steps)
                steps.pop()
                total_steps -= i
        
        backtrack([], 0)
        return len(res)
#####################################################################################
# time limit exceeded
# finding all combinations --> backtracking
class Solution3:
    def climbStairs(self, n: int) -> list[list[int]]:
        res = []
        
        # def backtrack(steps:list[int], total_steps:int):
        #     if total_steps == n:
        #         res.append(steps[:])
        #         return
        #     if total_steps > n:
        #         return

        #     for i in [1, 2]:
        #         steps.append(i)
        #         total_steps += i
        #         backtrack(steps, total_steps)
        #         steps.pop()
        #         total_steps -= i
        # backtrack([], 0)
        
        def backtrack(path: list[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return
            for step in [1, 2]:
                path.append(step)
                backtrack(path, remaining - step)
                path.pop()
        
        backtrack([], n)
        return res
#####################################################################################    
# dp
class Solution:
    def climbStairs(self, n: int) -> int:  
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2]) 
        return dp[n-1]
#####################################################################################
# dp
class Solution:
    def climbStairs(self, n: int) -> int:  
        if n <=3:
            return n
        
        prev2 = 2
        prev1 = 3
        for _ in range(4, n+1):
            cur = prev1 + prev2 
            prev2 = prev1
            prev1 = cur

        return cur
####################################################################################
# slightly more optimized
class Solution:
    def climbStairs(self, n: int) -> int:  
        if n <=3:
            return n
        
        prev2 = 2
        prev1 = 3
        for _ in range(4, n+1):
            prev2, prev1 = prev1, prev1+prev2

        return prev1
####################################################################################    
s = Solution3()
# print(s.climbStairs(2))
# # >>> 2
# print(s.climbStairs(3))
# >>> 3 
print(s.climbStairs(5))
# >>> 89