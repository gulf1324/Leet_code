Code: [Word Search.py](../../Solutions/Top%20100%20liked/Word%20Search.py)
# Example : 
```
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]], 
word = "SEE"
```

```python
exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
├── Start nested loops to try each position as starting point   # for loop
├── for (0,0): 'A' != 'S', continue
├── for (0,1): 'B' != 'S', continue
├── for (0,2): 'C' != 'S', continue
├── for (0,3): 'E' != 'S', continue
├── for (1,0): 'S' == 'S', call backtrack(1,0,0)
│   ├── backtrack(1,0,0): board[1][0]='S', word[0]='S', match
│   │   ├── Mark (1,0) as visited (board[1][0]='')
│   │   ├── if backtrack(2,0,1): Down
│   │   │   ├── board[2][0]='A', word[1]='E', no match
│   │   │   └── Return False
│   │   ├── if backtrack(0,0,1): Up
│   │   │   ├── board[0][0]='A', word[1]='E', no match
│   │   │   └── Return False
│   │   ├── if backtrack(1,1,1): Right
│   │   │   ├── board[1][1]='F', word[1]='E', no match
│   │   │   └── Return False
│   │   ├── if backtrack(1,-1,1): Left
│   │   │   ├── Out of bounds, invalid
│   │   │   └── Return False
│   │   ├── All directions failed, restore board[1][0]='S'
│   │   └── Return False  # Starting point "S" in board[1][0] ==> Failed
├── for (1,1): 'F' != 'S', continue
├── for (1,2): 'C' != 'S', continue
├── for (1,3): 'S' == 'S', call backtrack(1,3,0)   # Another starting point "S" in board[1][3] 
│   ├── backtrack(1,3,0): board[1][3]='S', word[0]='S', match
│   │   ├── Mark (1,3) as visited (board[1][3]='')
│   │   ├── if backtrack(2,3,1): Down
│   │   │   ├── backtrack(2,3,1): board[2][3]='E', word[1]='E', match
│   │   │   │   ├── Mark (2,3) as visited (board[2][3]='')
│   │   │   │   ├── if backtrack(3,3,2): Down
│   │   │   │   │   ├── Out of bounds, invalid
│   │   │   │   │   └── Return False
│   │   │   │   ├── if backtrack(1,3,2): Up
│   │   │   │   │   ├── board[1][3]='' (visited), no match
│   │   │   │   │   └── Return False
│   │   │   │   ├── if backtrack(2,4,2): Right
│   │   │   │   │   ├── Out of bounds, invalid
│   │   │   │   │   └── Return False
│   │   │   │   ├── if backtrack(2,2,2): Left
│   │   │   │   │   ├── backtrack(2,2,2): board[2][2]='E', word[2]='E', match
│   │   │   │   │   │   ├── k=3 equals len(word)=3
│   │   │   │   │   │   └── Return True  # WORD FOUND 
│   │   │   │   │   └── Return True 
│   │   │   │   └── Return True
│   │   │   └── Return True
│   │   └── Return True
└── Return True (Word "SEE" found in the board)     # Success
```