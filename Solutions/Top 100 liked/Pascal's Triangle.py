# Pascal's triangle (DP)
# 25 minutes, passed (100%/59%)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        
        for row_i in range(1, numRows):
            prev_row = res[row_i-1]
            if row_i == 1:
                res.append([1,1])
            
            else:
                temp_row = [0] * (row_i + 1)
                for val_i in range(0, len(temp_row)-1):
                    if val_i == 0: # first element
                        temp_row[val_i] = 1
                    else:
                        temp_row[val_i] = prev_row[val_i-1] +  prev_row[val_i] # middle element
                temp_row[-1] = 1 # last element
                
                res.append(temp_row[:])
        return res
############################################################################################
# optmized (DP) (100%/87%)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            prev = res[-1]
            curr_row = [1] # first element
            
            for j in range(1, len(prev)):
                curr_row.append(prev[j - 1] + prev[j]) # middle elements
            curr_row.append(1) # last element
            res.append(curr_row)
        
        return res
############################################################################################    
# not DP
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        
        for row_i in range(1, numRows):
            if row_i == 1:
                res.append([1,1])
            
            else:
                prev_row = res[row_i-1] + [0]
                curr_row = [0] + res[row_i-1]
                res.append([i + j for i,j in zip(prev_row, curr_row)])
        return res
############################################################################################
# not DP, optimized
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            prev = res[-1]
            res.append([i + j for i, j in zip([0]+prev, prev+[0])])
        return res
############################################################################################     
s = Solution()
print(s.generate(numRows = 5))
# >>> [[1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]]
        