class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        return results
##############################################################################################################################               
s = Solution()
print(s.dailyTemperatures(nums = [3,2,3,1,2,4,5,5,6], k = 4))
# >>> 4
print(s.dailyTemperatures(nums = [3,2,1,5,6,4], k = 2))
# >>> 5