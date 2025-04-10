class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        
        def DFS(queens:list[int], xy_dif:list[int], xy_sum:list[int]) -> None:
            row_i = len(queens)
            if row_i == n:
                result.append(queens)
                return
            for col_i in range(n):
                if (col_i not in queens) and (row_i - col_i not in xy_dif) and (row_i + col_i not in xy_sum): 
                    DFS(queens+[col_i], xy_dif+[row_i-col_i], xy_sum+[row_i+col_i])  
        
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
##############################################################################################################################               
s = Solution()
print(s.solveNQueens(4))
# >>> [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]