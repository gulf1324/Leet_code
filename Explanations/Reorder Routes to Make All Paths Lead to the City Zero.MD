## Reorder Routes to Make All Paths Lead to the City Zero
![Alt text](Reorder%20Routes%20to%20Make%20All%20Paths%20Lead%20to%20the%20City%20Zero.png "8 provinces")


```n = 6
connections = [[0,1], [1,3], [2,3], [4,0], [4,5]]
```

---

### 1. Build the graph:
```python
# Initial empty graph
graph = defaultdict(list)

# Adding edges:
# [0,1]: 
graph[0].append((1, 1))   # 0 -> 1
graph[1].append((0, 0))   # 1 <- 0

# [1,3]:
graph[1].append((3, 1))   # 1 -> 3
graph[3].append((1, 0))   # 3 <- 1

# [2,3]:
graph[2].append((3, 1))   # 2 -> 3
graph[3].append((2, 0))   # 3 <- 2

# [4,0]:
graph[4].append((0, 1))   # 4 -> 0
graph[0].append((4, 0))   # 0 <- 4

# [4,5]:
graph[4].append((5, 1))   # 4 -> 5
graph[5].append((4, 0))   # 5 <- 4
```

### 2. DFS tracing starting from city ```0```:
```python
dfs(0, -1)
├── Checking neighbors of 0: [(1, 1), (4, 0)]
│   ├── For (1, 1):
│   │   count += 1  # needs reversal
│   │   │
│   │   └── dfs(1, 0)
│   │       ├── Checking neighbors of 1: [(0, 0), (3, 1)]
│   │       │   ├── (0, 0) is parent, skip
│   │       │   └── For (3, 1):
│   │       │       count += 1  # needs reversal
│   │       │       │
│   │       │       └── dfs(3, 1)
│   │       │           ├── Checking neighbors of 3: [(1, 0), (2, 0)]
│   │       │           │   ├── (1, 0) is parent, skip
│   │       │           │   └── For (2, 0):
│   │       │           │       count += 0  # no reversal needed
│   │       │           │       └── dfs(2, 3) returns 0
│   │       │           └── Returns 0
│   │       └── Returns 1
│   │
│   └── For (4, 0):
│       count += 0  # no reversal needed
│       │
│       └── dfs(4, 0)
│           ├── Checking neighbors of 4: [(0, 1), (5, 1)]
│           │   ├── (0, 1) is parent, skip
│           │   └── For (5, 1):
│           │       count += 1  # needs reversal
│           │       └── dfs(5, 4) returns 0
│           └── Returns 1
└── Returns 3
```
---
> ### The goal is to reorient edges so all cities can be reached from city 0. 
>- Uses DFS to traverse from city 0
>- Whenever it encounters an edge in its original direction (marked by 1), it needs to be reversed
>- When it encounters an edge in reverse direction (marked by 0), no action needed
>- Skips the parent node to avoid going back
>- Accumulates the total number of edges that need to be reversed
---