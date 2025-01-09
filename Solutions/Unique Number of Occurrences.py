class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        res = {}
        for num in arr:
            res[num] = res.get(num, 0) + 1
        return len(res) == len(set(res.values()))

s = Solution()
print(s.uniqueOccurrences([1,2]))
