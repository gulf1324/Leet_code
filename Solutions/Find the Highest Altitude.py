class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        cur_altitude = 0
        max_altitude = cur_altitude
        for diff in gain:
            cur_altitude = cur_altitude + diff
            max_altitude = max(cur_altitude,max_altitude)
        return max_altitude
    
s = Solution()
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))
