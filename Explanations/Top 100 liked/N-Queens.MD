Code: [N-Queens.py](../../Solutions/Top%20100%20liked/N-Queens.py)
# Example : 
```
n = 4
```
![Alt text](N-Queens.jpg)
---

```python
DFS([], [], [])
│
├── row_i = 0, col_i = 0 → safe → DFS([0], [0], [0])
│   ├── row_i = 1, col_i = 0 → conflict → skip # col_i not in queens == False
│   ├── row_i = 1, col_i = 1 → conflict → skip # row_i - col_i not in xy_dif == False
│   ├── row_i = 1, col_i = 2 → safe → DFS([0, 2], [0, -1], [0, 3])
│   │   ├── row_i = 2, col_i = 0 → conflict → skip # col_i not in queens == False
│   │   ├── row_i = 2, col_i = 1 → conflict → skip # row_i + col_i not in xy_sum == False
│   │   ├── row_i = 2, col_i = 2 → conflict → skip # col_i not in queens == False
│   │   └── row_i = 2, col_i = 3 → conflict → skip # row_i - col_i not in xy_dif == False
│   └── row_i = 1, col_i = 3 → safe → DFS([0, 3], [0, -2], [0, 4])
│       ├── row_i = 2, col_i = 0 → conflict → skip # col_i not in queens == False
│       ├── row_i = 2, col_i = 1 → safe → DFS([0, 3, 1], [0, -2, 1], [0, 4, 3])
│       │   ├── row_i = 3, col_i = 0 → conflict → skip # col_i not in queens == False
│       │   ├── row_i = 3, col_i = 1 → conflict → skip # col_i not in queens == False
│       │   ├── row_i = 3, col_i = 2 → conflict → skip # row_i - col_i not in xy_dif == False
│       │   └── row_i = 3, col_i = 3 → conflict → skip # col_i not in queens == False
│       ├── row_i = 2, col_i = 2 → conflict → skip # row_i - col_i not in xy_dif == False
│       └── row_i = 2, col_i = 3 → conflict → skip # col_i not in queens == False
│
├── row_i = 0, col_i = 1 → safe → DFS([1], [-1], [1])
│   ├── row_i = 1, col_i = 0 → conflict → skip # row_i + col_i not in xy_sum == False
│   ├── row_i = 1, col_i = 1 → conflict → skip # col_i not in queens == False
│   ├── row_i = 1, col_i = 2 → conflict → skip # row_i - col_i not in xy_dif == False
│   └── row_i = 1, col_i = 3 → safe → DFS([1, 3], [-1, -2], [1, 4])
│       ├── row_i = 2, col_i = 0 → safe → DFS([1, 3, 0], [-1, -2, 2], [1, 4, 2])
│       │   ├── row_i = 3, col_i = 0 → conflict → skip # col_i not in queens == False
│       │   ├── row_i = 3, col_i = 1 → conflict → skip # row_i - col_i not in xy_dif == False
│       │   ├── row_i = 3, col_i = 2 → safe → DFS([1, 3, 0, 2], [-1, -2, 2, 1], [1, 4, 2, 5])
│       │   │   └── len == n → append [1, 3, 0, 2]
│       │   └── row_i = 3, col_i = 3 → conflict → skip # col_i not in queens == False
│       ├── row_i = 2, col_i = 1 → conflict → skip # col_i not in queens == False
│       ├── row_i = 2, col_i = 2 → conflict → skip # row_i + col_i not in xy_sum == False
│       └── row_i = 2, col_i = 3 → conflict → skip # col_i not in queens == False
│
├── row_i = 0, col_i = 2 → safe → DFS([2], [-2], [2])
│   ├── row_i = 1, col_i = 0 → safe → DFS([2, 0], [-2, 1], [2, 1])
│   │   ├── row_i = 2, col_i = 0 → conflict → skip # col_i not in queens == False
│   │   ├── row_i = 2, col_i = 1 → conflict → skip # row_i - col_i not in xy_dif == False
│   │   ├── row_i = 2, col_i = 2 → conflict → skip # col_i not in queens == False
│   │   └── row_i = 2, col_i = 3 → safe → DFS([2, 0, 3], [-2, 1, -1], [2, 1, 5])
│   │       ├── row_i = 3, col_i = 0 → conflict → skip # col_i not in queens == False
│   │       ├── row_i = 3, col_i = 1 → safe → DFS([2, 0, 3, 1], [-2, 1, -1, 2], [2, 1, 5, 4])
│   │       │   └── len == n → append [2, 0, 3, 1]
│   │       ├── row_i = 3, col_i = 2 → conflict → skip # col_i not in queens == False
│   │       └── row_i = 3, col_i = 3 → conflict → skip # col_i not in queens == False
│   ├── row_i = 1, col_i = 1 → conflict → skip # row_i + col_i not in xy_sum == False
│   ├── row_i = 1, col_i = 2 → conflict → skip # col_i not in queens == False
│   └── row_i = 1, col_i = 3 → conflict → skip # row_i - col_i not in xy_dif == False
│
└── row_i = 0, col_i = 3 → safe → DFS([3], [-3], [3])
    ├── row_i = 1, col_i = 0 → safe → DFS([3, 0], [-3, 1], [3, 1])
    │   ├── row_i = 2, col_i = 0 → conflict → skip # col_i not in queens == False
    │   ├── row_i = 2, col_i = 1 → conflict → skip # row_i - col_i not in xy_dif == False
    │   ├── row_i = 2, col_i = 2 → safe → DFS([3, 0, 2], [-3, 1, 0], [3, 1, 4])
    │   │   ├── row_i = 3, col_i = 0 → conflict → skip # col_i not in queens == False
    │   │   ├── row_i = 3, col_i = 1 → conflict → skip # row_i + col_i not in xy_sum == False
    │   │   ├── row_i = 3, col_i = 2 → conflict → skip # col_i not in queens == False
    │   │   └── row_i = 3, col_i = 3 → conflict → skip # row_i - col_i not in xy_dif == False
    │   └── row_i = 2, col_i = 3 → conflict → skip # col_i not in queens == False
    ├── row_i = 1, col_i = 1 → safe → DFS([3, 1], [-3, 0], [3, 2])
    │   ├── row_i = 2, col_i = 0 → conflict → skip # row_i + col_i not in xy_sum == False
    │   ├── row_i = 2, col_i = 1 → conflict → skip # col_i not in queens == False
    │   ├── row_i = 2, col_i = 2 → conflict → skip # row_i - col_i not in xy_dif == False
    │   └── row_i = 2, col_i = 3 → conflict → skip # col_i not in queens == False
    ├── row_i = 1, col_i = 2 → conflict → skip # row_i + col_i not in xy_sum == False
    └── row_i = 1, col_i = 3 → conflict → skip # col_i not in queens == False
