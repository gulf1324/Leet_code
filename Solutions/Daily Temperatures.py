##########################################################################
# Time limit exceeded
class Solution1:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        p, q = 0, 1
        while p < len(temperatures)-1:
            if p < q:
                if temperatures[p] < temperatures[q]:
                    ans[p] = q-p
                    p += 1
                    q = p+1
                else:
                    if q == len(temperatures)-1:
                        p +=1
                        q = p+1
                    else:
                        q += 1
        return ans
####################################################################################
# Correct
# for/ while
# ==> for every element:
#        while conditioned: 
#           assign index of `result` list
#        register every element into the checking "stack"
class Solution2:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        return results
####################################################################################

s = Solution2()
print(s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
# >>> [1,1,4,2,1,1,0,0]
print(s.dailyTemperatures(temperatures = [30,40,50,60]))
# >>> [1,1,1,0]
print(s.dailyTemperatures(temperatures = [55,38,53,81,61,93,97,32,43,78]))
# >>> [3,1,1,2,1,1,0,1,1,0]
# Solution1 [3,1,1,2,1,1,0,0,0,0]
