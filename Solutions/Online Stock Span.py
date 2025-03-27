# keep adding '(previous-stack's)day' to current day until 
# no '(previous-stack's)price' is larger than current price
class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        day = 1
        while self.stack and price >= self.stack[-1][-1]:
            #############################
            day += self.stack.pop()[0] ##
            #############################
        self.stack.append([day, price])
        return day
################################################################################################
s = StockSpanner()
queries = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
inputs = [[], [100], [80], [60], [70], [60], [75], [85]]
ans = [None]
for query, input in zip(queries[1:], inputs[1:]):
    if query == 'next':
        ans.append(s.next(input[0]))

print(ans)
# >>> [None, 1, 1, 1, 2, 1, 4, 6]