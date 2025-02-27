from collections import defaultdict
########################################################################################################
# Using dictionary
# Wrong approach(+ not wrong, not enough post process)
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        dic = defaultdict(set)
        for i, (num1, num2) in enumerate(zip(nums1, nums2)):
            dic[i] = (num1, num2) # dic[index] = (num1, num2)
        # ex) 0: (2, 11), 1: (1, 7), 2: (14, 13), 3: (12, 6)})

        # sort by nums2(pair nums1), keep index as key, keep only kth largest of nums2
        sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1][1], reverse=True)[:k])
        # ex) {2: (14, 13), 0: (2, 11), 1: (1, 7)}

        return sum([i[0] for i in sorted_dic.values()]) * min([j[1] for j in sorted_dic.values()])    
########################################################################################################
import heapq
# more on to Soluion1/ efficient
# defaultdict => pairs of list(no need of index) 
# - nums1 index => heappush/heappop
# - nums2 index => sorted/ k-1 index all the time
class Solution2:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # pairs of (nums2[i], nums1[i]) and sort by nums2 in descending order
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        # heapq for num1
        min_heap = []
        
        # Extract the sorted values
        sorted_nums2 = [pair[0] for pair in pairs]
        sorted_nums1 = [pair[1] for pair in pairs]
        
        # Initialize sum
        total_sum = 0
        for i in range(k):
            heapq.heappush(min_heap, sorted_nums1[i])
            total_sum += sorted_nums1[i]
        
        # sorted_nums2[k-1] == min(sorted_nums2)
        max_score = total_sum * sorted_nums2[k-1]
        
        # Try elements beyond the first k
        for i in range(k, len(nums1)):
            # update sum(sorted_nums1)
            total_sum += sorted_nums1[i]
            heapq.heappush(min_heap, sorted_nums1[i])
            smallest = heapq.heappop(min_heap)
            total_sum -= smallest

            # Update(check) max_score 
            score = total_sum * sorted_nums2[i]
            max_score = max(max_score, score)
        
        return max_score
########################################################################################################
# Best
class Solution3:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Sort by nums2 descending
        num_pairs = sorted(zip(nums2, nums1), reverse=True)  

        heap = []
        max_score = 0
        nums1_sum = 0

        for num2, num1 in num_pairs:
            nums1_sum += num1
            heapq.heappush(heap, num1)

            if len(heap) > k:  
                smallest = heapq.heappop(heap)
                nums1_sum -= smallest
            
            if len(heap) == k: 
                max_score = max(max_score, num2 * nums1_sum)
        
        return max_score
########################################################################################################        
s = Solution3()
# print(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
# >>>  12

print(s.maxScore(nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3))
# >>> 168 (but mine 119)
# Solution2 >>> 168