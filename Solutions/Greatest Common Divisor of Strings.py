# "ABCABC", "ABC"
# >>> "ABC"
# "ABABAB", "ABAB"
# >>> "AB"
# "ABABABAB", "ABAB"
# >>> "ABAB"
# "ABCDEF", "ABC"
# >>> ""
#####################################################################
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find gcd_len
        gcd_len = 0
        sol = ""
        for i in range(1, max(len(str1), len(str2))+1):
            if (len(str1)%i ==0) and (len(str2)%i==0):
                if i > gcd_len:
                    gcd_len = i
        
        # get gcd_str window and scan
        gcd_str = str1[:gcd_len]
        check_str = str1 + str2
        for window in range(0,len(str1+str2), gcd_len):
            if gcd_str != check_str[0+window:window +gcd_len]:
                return ""
            else:
                sol = gcd_str
        return sol
#####################################################################
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find gcd_len
        gcd_len = 0
        for i in range(1, max(len(str1), len(str2))+1):
            if (len(str1)%i ==0) and (len(str2)%i==0):
                if i > gcd_len:
                    gcd_len = i
        if str1 + str2 != str2 + str1:
            return ""
        else:
            return str1[:gcd_len]
#####################################################################

sol = Solution2()
a = sol.gcdOfStrings("ABABAB", "ABAB")
print(a)
