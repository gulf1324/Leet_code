# My solution
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res =  []
        
        def backtrack(total:int, combination:list) -> None:
            if len(combination) == n*2:
                if total == 0:
                    res.append(''.join(combination))
                    return
                
                # if total != 0:
                #     return 
                # ==> pre-determined
                
            # ex) n= 3, "(((("
            if combination.count("(") > n :
                return
            
            # ex) "(()))"
            if total < 0 :
                return

            for parenthesis in ["(", ")"]:
                # The += operator’s behavior with lists is equivalent to extend()
                # combination += parenthesis
                combination.append(parenthesis)
                total += 1 if parenthesis == "(" else -1
                backtrack(total, combination)
                pop = combination.pop()
                total -= 1 if pop == "(" else +1             
        
        backtrack(1, ["("])
        return res
########################################################################################
# More readable, efficient
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(opened, closed, prefix):
            if opened == closed == n:
                result.append(prefix)
                return result
            
            if opened + 1 <= n:
                backtrack(opened + 1, closed, prefix + '(')
            
            if closed + 1 <= opened:
                backtrack(opened, closed + 1, prefix + ')')
            return result
        
        return backtrack(0, 0, "")
########################################################################################
s = Solution()
print(s.generateParenthesis(3))
# >>> ['((()))', '(()())', '(())()', '()(())', '()()()']