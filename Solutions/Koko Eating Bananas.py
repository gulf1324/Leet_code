class Solution:
    def total_time_needed(self, speed: int, piles:list[int]) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours 

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right 
        while left <= right:
            mid = (left + right) // 2
            if self.total_time_needed(mid, piles) <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result


s = Solution()
print(s.minEatingSpeed(piles = [3,6,7,11], h = 8))
# print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
# >>> 4