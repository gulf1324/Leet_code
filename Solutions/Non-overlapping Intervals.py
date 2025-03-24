class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float("-inf")
        overlap = 0
        for i, j in intervals:
            if i >= end: 
                end = j
            else: 
                overlap += 1
        return overlap
####################################################################################
s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))