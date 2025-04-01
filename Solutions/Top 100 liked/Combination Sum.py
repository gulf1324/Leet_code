# My solution
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(combination:list) -> None:
            if sum(combination) == target and sorted(combination) not in res:
                res.append(sorted(combination))
                return
            
            if sum(combination) > target:
                return
            
            for num in candidates:
                combination.append(num)
                backtrack(combination)
                combination.pop()

        backtrack([])
        return res
#####################################################################################################
# sum() calls on every backtracking --> keep track of curr_sum
# trying all combinations in for loop --> sort array & from start to len(candidates)
# elements of combinations can be duplicates -> backtrack(..., "i(not i+1)", ...)

# More efficient
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def backtrack(current_sum:int, index:int, combination:list[int]) -> None:
            if current_sum == target:
                res.append(combination[:])
                return
            
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if current_sum + candidates[i] > target:
                    break
                combination.append(candidates[i])
                backtrack(current_sum + candidates[i], i, combination) ######
                combination.pop()

        backtrack(0, 0, [])
        return res
#####################################################################################################
s = Solution()
print(s.combinationSum(candidates = [2,3,5], target = 8))
# >>> [[2,2,2,2],[2,3,3],[3,5]]