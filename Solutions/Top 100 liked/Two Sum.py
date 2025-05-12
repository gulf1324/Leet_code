# time limit exceeded
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        combinations = []
        self.res = []
        
        def bt(index:int , combinations:list[int], target:int):  
            if len(combinations) == 2 and sum(x[1] for x in combinations) == target:
                self.res = [x[0] for x in combinations]
                return
            if len(combinations) > 2:
                return
            
            for i in range(index, len(nums)):
                combinations.append((i, nums[i]))
                if self.res != []:
                    break
                bt(i+1, combinations, target)
                combinations.pop()

        bt(0, combinations, target)
        return self.res
#####################################################################################################
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[nums[i]] = i

        return []
#####################################################################################################    
s = Solution2()
print(s.twoSum(nums = [2,7,11,15], target = 9))
# >>> [0,1]
print(s.twoSum(nums = [3,2,4], target = 6))
# >>> [1,2]