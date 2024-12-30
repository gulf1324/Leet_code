# "the sky is blue"
# >>> "blue is sky the"
# "  hello world  "
# >>> "world hello"
# "a good   example"
# >>> "example good a"
####################################################################
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        s_reversed = s_list[::-1]
        res_list = [word for word in s_reversed if word != ""]
        return " ".join(res_list)
####################################################################
# .split() default separator ==> whitespace
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        return " ".join(s_list[::-1])
    

