# bit-wise idea
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        for i in range(2**n):
            combinations = []
            bin_selection = format(i, f'0{n}b')
            
            for i, selection in enumerate(bin_selection):
                if selection == '0':
                    continue
                else:
                    combinations.append(nums[i])

            res.append(combinations[:])
        return res
#####################################################################################
# optimized    
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        
        for i in range(2**n):  # ex) 5(101)
            combination = []
            for j in range(n): # j --> 0,1,2
                if i & (1 << j):  
                    # ex) 101 & (1 << 0) ==> 101 & 1(=001) ==> 001 ==> 1 ==> True
                    # ex) 101 & (1 << 1) ==> 101 & 10(=010) ==> 000 ==> 0 ==> False
                    # ex) 101 & (1 << 2) ==> 101 & 100(=100) ==> 100 ==> 4 ==> True
                    combination.append(nums[j])
            res.append(combination)
        
        return res
#####################################################################################
# backtrack
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        
        def backtrack(start):
            res.append(subset[:])
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return res
#####################################################################################
s = Solution()
print(s.subsets(nums = [1,2,3]))