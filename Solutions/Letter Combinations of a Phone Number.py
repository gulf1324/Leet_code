################################################################################
# recursive
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            
            for char in phone_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()  # "Backtracking"

        backtrack(0, [])
        return result
################################################################################
# iterative (BFS)
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        # (index, current_path)
        queue = deque([(0, [])])
        
        while queue:
            index, path = queue.popleft()  # popleft() -> BFS
            
            # Base case: if we've processed all digits
            if index == len(digits):
                result.append("".join(path))
                continue
            
            # Get the current digit we're processing
            digit = digits[index]
            
            for char in phone_map[digit]:
                queue.append((index + 1, path + [char]))
        
        return result
################################################################################
s = Solution()
print(s.letterCombinations(digits = "23"))
# print([ i for i in s.letterCombinations(digits = "23")])