# correct idea, wrong algorithm
# if i in coins, == 1
# if i not in coins, == dp
# first thought was to use popleft() for coins to prevent meaningless iterations.
from collections import deque
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort()
        coins = deque(coins)
        dp = [0] * (amount +1)
        max_coin = coins[0]
        for i in range(1, len(dp)):
            if i in coins:
                dp[i] = 1
                max_coin = coins.popleft()
            else:
                if dp[i-max_coin] == -1 or i < max_coin:
                    dp[i] = -1
                else:
                    dp[i] = 1 + dp[i-max_coin]
        return dp[amount]
##################################################################################
# 
# `i in coins` , `else` to
# --> double for loops
#
# `coins = deque(coins)` , coins.popleft()
# --> **Constraints** was 
# * 1 <= coins.length <= 12
# * 0 <= amount <= 10^4
# --> double for loop is fine.
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        # Compute minimum coins needed for all amounts up to 'amount'
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Check if solution exists
        return dp[amount] if dp[amount] != MAX else -1
##################################################################################
from collections import deque
# as effecient as dp
# BFS
# only access to reachable path <-> dp (fill up from 0 to amount)
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        queue = deque([(0, 0)])  # (current_amount, num_coins)
        visited = {0}
        
        while queue:
            curr_amount, num_coins = queue.popleft()
            
            for coin in coins:
                next_amount = curr_amount + coin
                
                if next_amount == amount:
                    return num_coins + 1
                
                if next_amount < amount and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, num_coins + 1))
                    
        return -1
##################################################################################        
s = Solution()
print(s.coinChange(coins = [1,2,5], amount = 11))
# >>> 3
print(s.coinChange(coins = [2], amount = 3))
# >>> -1
print(s.coinChange(coins = [2147483647], amount = 2))
# >>> index out of range `dp[i-max_coin] `
# >>> -1
print(s.coinChange(coins = [1,2,5], amount = 5))
# >>> 1