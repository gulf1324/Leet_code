class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] 
        for character in s:
            if character =='*':
                stack.pop()
            else:
                stack.append(character)
        return "".join(stack)

s = Solution()
print(s.removeStars("leet**cod*e"))