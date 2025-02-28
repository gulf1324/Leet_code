import heapq
########################################################################################################
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        heap_1 = []
        heap_2 = []
        res = 0
        
        # len(costs) == 35 < 2 * candidates, resulting in half-half to heap_1 and heap_2
        for i in range(candidates):
            if any(costs):
                heapq.heappush(heap_1, costs[i])
                heapq.heappush(heap_2, costs[-i-1])
                costs[i], costs[-i-1] = None, None
        # in last loop,
        # heap_1 = [..., 25(exact middle element)]
        # heap_2 = [..., 25(exact middle element)]
        
        heap_1_i, heap_2_i = i+1, i+1
        while k > 0 :
            for _ in range(i, len(costs)):
                if heap_1[0] <= heap_2[0]:
                    res += heapq.heappop(heap_1)
                    if costs[heap_1_i]:
                        heapq.heappush(heap_1, costs[heap_1_i])
                        costs[heap_1_i] = None
                        heap_1_i +=1
                else:
                    res += heapq.heappop(heap_2)
                    if costs[-heap_2_i-1]:
                        heapq.heappush(heap_2, costs[-heap_2_i-1])
                        costs[-heap_2_i-1] =  None
                        heap_2_i +=1 
                k -= 1
                if k == 0:
                    return res
        return res
########################################################################################################
s = Solution()
# print(s.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
# # # >>> 11

# print(s.totalCost(costs = [1,2,4,1], k = 3, candidates = 3))
# # 4 

# print(s.totalCost(costs =[31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k =11, candidates =2))
# # 423 (but 430)

print(s.totalCost(costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75],
                   k = 13, candidates = 23))
# 223 (but 222)