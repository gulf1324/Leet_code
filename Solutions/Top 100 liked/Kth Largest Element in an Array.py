import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
##############################################################################################################################               
s = Solution()
print(s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
# >>> 4
print(s.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
# >>> 5