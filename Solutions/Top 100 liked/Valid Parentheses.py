class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            # open bracket
            if char in mapping.values():
                stack.append(char)
            
            # close bracket
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return stack == []
###################################################################
s = Solution()
print(s.isValid("()[]{}"))
# >>> True
print(s.isValid("([])"))
# >>> True
print(s.isValid("(]"))
# >>> False