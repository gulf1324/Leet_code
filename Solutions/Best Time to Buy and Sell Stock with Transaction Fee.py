class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        balance = float('-inf')
        profit = 0
        
        for price in prices:
            balance = max(balance, profit - price)
            profit = max(profit, balance + price - fee)
        
        return profit
####################################################################
s = Solution()
print(s.maxProfit(prices = [1,3,2,8,4,9], fee = 2))
# >>> 8