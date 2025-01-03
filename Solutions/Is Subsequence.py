#############################################################
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        while s_pointer < len(s) and t_pointer < len(t) :
            if s[s_pointer] == t[t_pointer]:
                s_pointer +=1
                t_pointer +=1
            elif s[s_pointer] != t[t_pointer]:
                t_pointer +=1
        return s_pointer == len(s)
#############################################################
# Slightly more optimized
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        while s_pointer < len(s) and t_pointer < len(t) :
            if s[s_pointer] == t[t_pointer]:
                s_pointer +=1
            t_pointer +=1
        return s_pointer == len(s)
#############################################################
# Slightly more efficient due to:
# early exit, 
# less overhead comparing to 2 bound checking every iteration
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        for t_pointer in range(len(t)):
            if s_pointer == len(s):
                return True
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
        return s_pointer == len(s)
#############################################################

s = Solution()
print(s.isSubsequence("axc","ahbgdc"))
