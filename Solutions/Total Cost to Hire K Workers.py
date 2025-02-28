import heapq
from collections import defaultdict
########################################################################################################
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        heap_1 = []
        heap_2 = []
        res = 0
        
        while k > 0 :
            for i in range(len(costs)):
                if len(heap_1) < candidates and len(heap_2) < candidates and any(costs):
                    heapq.heappush(heap_1, costs[i])
                    heapq.heappush(heap_2, costs[-i-1])
                    costs[i], costs[-i-1] = None, None
                
                # can't track index fairly across heap_1, heap_2(might skip some elements)
                else:
                    if heap_1[0] <= heap_2[0]:
                        res += heapq.heappop(heap_1)
                        if costs[i]:
                            heapq.heappush(heap_1, costs[i])
                            costs[i] = None
                    else:
                        res += heapq.heappop(heap_2)
                        if costs[-i-1]:
                            heapq.heappush(heap_2, costs[-i-1])
                            costs[-i-1] =  None
                    k -= 1
                
                if k == 0:
                    return res
        return res        
########################################################################################################
s = Solution()
# print(s.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
# # >>> 11

# print(s.totalCost(costs = [1,2,4,1], k = 3, candidates = 3))
# 4 

print(s.totalCost(costs =[31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k =11, candidates =2))
# 423 (but 430)