class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda p: p[1])
        ans, arrow = 0, 0
        for [start, end] in points:
            if ans == 0 or start > arrow:
                ans += 1 
                arrow = end
        return ans
#################################################################
s = Solution()
# print(s.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
# # # >>> 2
# print(s.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))
# # >>> 2
# print(s.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
# # >>> 4 
print(s.findMinArrowShots(points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
# >>> 2