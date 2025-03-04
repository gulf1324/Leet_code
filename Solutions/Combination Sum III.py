#######################################################################################################
# my solution
class Solution1:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        nums = [1,2,3,4,5,6,7,8,9]
        
        def backtrack(index, combination):
            if len(combination) == k and sum(combination) == n:
                res.append(combination[:])
                return
            else:
                for num in nums[index:]:
                    # prevents duplicate ( ex) [1, 3, 3] )
                    if num > (combination[-1] if combination else 0):
                        
                        combination.append(num)
                        backtrack(index+1, combination)
                        combination.pop()

        backtrack(0,[])
        return res
#######################################################################################################
# More efficient
# 1. Early pruning of recursive branches
# 2. sum() every time => keep track of curr_sum as an additional variable
class Solution2:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        def backtrack(index, combination, curr_sum):
            if len(combination) == k:
                if curr_sum == n:
                    res.append(combination[:])
                return
            
            # 1. Early pruning
            if len(combination) > k or curr_sum >= n:  
                return
                
            for num in nums[index:]:
                if num > (combination[-1] if combination else 0):
                    combination.append(num)
                    
                    # 2. keep track of curr_sum
                    backtrack(index + 1, combination, curr_sum + num)  
                    combination.pop()

        backtrack(0, [], 0)  # Start with curr_sum = 0
        return res
#######################################################################################################
# More efficient
# 3. for num in nums[index:]:  =>  for i in range(index, len(nums)): 
#                                      num = nums[i]
#
#  - nums[index:] creates a slice (a new list) of the original array,
#    which uses extra memory 
#  - with this change, ```if num > (combination[-1] if combination else 0):``` becomes redundant
# 
# 4. Remove ```if num > (combination[-1] if combination else 0):```
#
#  - it's useless when backtracking recursion starts index with i + 1

"""
Solution2 vs Solution3 in regards with:
```if num > (combination[-1] if combination else 0):```

- Solution2 needs it because: index + 1 of backtracking recursion comes from 'initial' index(“Fixed starting index increment”),
                              allowing duplicates without filtering.
- Solution3 doesn't need it because: index + 1 of backtracking recursion comes from 'ongoing' index(“Choice-driven index increment”),
                                     ensuring distinctness naturally.
"""
class Solution3:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        def backtrack(index, combination, curr_sum):
            if len(combination) == k:
                if curr_sum == n:
                    res.append(combination[:])
                return
            
            if len(combination) > k or curr_sum >= n:  
                return

            # 3. less memory than list slicing
            for i in range(index, len(nums)):
                num = nums[i]
                # if num > (combination[-1] if combination else 0):
                combination.append(num)
                backtrack(i + 1, combination, curr_sum + num)  
                combination.pop()

        backtrack(0, [], 0) 
        return res 
#######################################################################################################
# Best
# nums => range / 10
class Solution4:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        def backtrack(index, combination, curr_sum):
            if len(combination) == k and curr_sum == n:
                res.append(combination[:])
                return
            
            if len(combination) >= k or curr_sum >= n:  
                return

            for i in range(index, 10):
                combination.append(i)
                backtrack(i + 1, combination, curr_sum + i)  
                combination.pop()

        backtrack(1, [], 0) 
        return res 
#######################################################################################################
s = Solution2()
print(s.combinationSum3(k = 2, n = 6))
# print(s.combinationSum3(k = 3, n = 7))
# print(s.combinationSum3(k = 3, n = 9))
# print(s.combinationSum3(k = 4, n = 1))