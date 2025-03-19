########################################################################################
# Wrong
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        checker = a | b
        max_len = max(len(bin(checker)), len(bin(c)))
        ans = 0
        
        checker = bin(checker)[2:].rjust(max_len, '0')
        c = bin(c)[2:].rjust(max_len, '0')
        for i in range(max_len-1, 0, -1):
            p = checker[i]
            q = c[i]
            if p != q:
                if p== '1' and q == '0':
                    ans += 2 
                elif p == '0' and q == '1':
                    ans += 1
        return ans
########################################################################################
class Solution2:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab, equal, ans = a | b, (a | b) ^ c, 0
        for i in range(31):
            mask = 1 << i
            if equal & mask:
                # ans += 1 if (ab & mask) < (c & mask) or (a & mask) != (b & mask) else 2
                ans += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
        return ans
########################################################################################
# := assigning and expression at the same time
class Solution3:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        minimal number of flips to transform 
        (a | b) -> c

        1. (a | b)^c => initial intuition just to find the difference
                        between (a|b) and c
                     => assign this to k at the same time with `:=` for 
                        efficiency
        
        2. (a|b) => 1 could be:
            1 - either a OR b has 1 => in this case, flip +2
            2 - both a AND b has 1 => in this case, flip +1
        
        3. for this problem, => (a & b & ( (a | b)^c(==k) )) because:
            this additional step shows:
                1 - position via `&k`
                2 - where both a AND b should be flipped via `a&b`
            
            all combined, a&b&k => additional +1 for the 2-2 case.
        """
        return (k := (a | b) ^ c).bit_count() + (a & b & k).bit_count()
########################################################################################
# most simplified
class Solution4:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        almost identical to Solution3, but used ~c instead.
        (a & b & ~c) => a AND b is 1, AND c is 0
        """
        return ((a | b) ^ c).bit_count() + (a & b & ~c).bit_count()
########################################################################################
s = Solution4()
print(s.minFlips(a = 8, b = 3, c = 5))
print(s.minFlips(a = 2, b = 6, c = 5))