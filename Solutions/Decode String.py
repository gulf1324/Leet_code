class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        num = 0

        for char in s:
            if char.isdigit():
                # num => num for next alphabet character
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, num))
                current_string = ""
                num = 0
            elif char == ']':
                last_string, last_num = stack.pop()
                ##########################################################
                current_string = last_string + last_num * current_string #
                ##########################################################
            else:
                current_string += char

        return current_string

s = Solution()
print(s.decodeString("3[a2[c]]"))
# >>> "accaccacc"
# 1. [('',3),('a',2)]   / ('c', 0)
# 2. [('',3)]           / a  + 2*c
# 3. []                 / '' + 3*acc