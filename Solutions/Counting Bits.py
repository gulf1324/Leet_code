################################################################
# Base case 
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(n, 0, -1):
            ans[i] = i.bit_count()
        return ans
################################################################
# Brian Kernighan’s algorithm
class Solution:    
    def count_bits(self, n):
        count = 0
        while n:
            n &= n - 1  
            count += 1
            # ex) 7 (+1)-> 6(+1) -> 4(+1) -> 0 ==> 3
        return count
    
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(len(ans)):
            ans[i] = self.count_bits(i)
        return ans 
################################################################            
# Pattern based O(n) 
# Explanation
class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        for i in range(1, n + 1):
            if i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[-1] + 1)
        return res
################################################################            
s =Solution()
print(s.countBits(7))