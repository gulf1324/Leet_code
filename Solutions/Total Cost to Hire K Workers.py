import heapq
########################################################################################################
# Correct 
# correct: 
#  - Use 2 heaps(head, tail) / (no duplicates)
#  - Keeps track of both heaps' indexes

# fixed:
#  - hiring process can happen only on one-side continuously. in this case, should check 
#    whether the heap is empty.
#  - left < right checks if there's any element left in ```costs```if so, should 
#    be pushed to either left/right heap.
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        # base case
        if len(costs) <= 2*candidates:  
            return sum(sorted(costs)[:k])

        n = len(costs)
        left_heap, right_heap = [], []
        left_i, right_i = 0, n - 1
        total_cost = 0

        # (value, index)
        for _ in range(candidates):
            if left_i <= right_i:
                heapq.heappush(left_heap, (costs[left_i], left_i))
                left_i += 1
            if left_i <= right_i:
                heapq.heappush(right_heap, (costs[right_i], right_i))
                right_i -= 1

        # Hiring process
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost, idx = heapq.heappop(left_heap)
                if left_i <= right_i:
                    heapq.heappush(left_heap, (costs[left_i], left_i))
                    left_i += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                if left_i <= right_i:
                    heapq.heappush(right_heap, (costs[right_i], right_i))
                    right_i -= 1
            
            total_cost += cost

        return total_cost
########################################################################################################
s = Solution()
print(s.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
# # # # >>> 11

# print(s.totalCost(costs = [1,2,4,1], k = 3, candidates = 3))
# # 4 

# print(s.totalCost(costs =[31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k =11, candidates =2))
# # 423 (but 430)

# print(s.totalCost(costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75],
#                    k = 13, candidates = 23))
# 223 (but 222)

print(s.totalCost(costs = [69,10,63,24,1,71,55,46,4,61,78,21,85,52,83,77,42,21,73,2,80,99,98,89,55,94,63,50,43,62,14],
                    k = 21, candidates = 31))

# (out of index Index Error)