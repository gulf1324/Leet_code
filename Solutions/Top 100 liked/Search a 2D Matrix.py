# 27 minutes, passed (100%/93%)
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix) -1
        col_left, col_right = 0, len(matrix[0]) - 1
        
        while row_left <= row_right:
            mid_row = (row_left + row_right)//2
            
            if matrix[mid_row][0] <= target:
                row_left = mid_row + 1
            if matrix[mid_row][0] > target:
                row_right = mid_row - 1
            
        target_row = matrix[row_right]

        while col_left <= col_right:
            mid = (col_left + col_right)//2
            if target_row[mid] == target:
                return True
            if target_row[mid] < target:
                col_left = mid + 1
            if target_row[mid] > target:
                col_right = mid -1 
        return False
########################################################################################
s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],
                               [10,11,16,20],
                               [23,30,34,60]],
                     target = 3))
# >>> True

print(s.searchMatrix(matrix = [[1,3,5,7],
                               [10,11,16,20],
                               [23,30,34,60]],
                     target = 13))
# >>> False
        