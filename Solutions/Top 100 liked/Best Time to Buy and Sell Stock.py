# My solution greedy
# 7 minutes, passed (63%/95%)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(price - min_price, max_profit)
        return max_profit
###################################################################                
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
# >>> 5