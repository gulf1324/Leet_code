# Code: [Subsets.py](../../Solutions/Top%20100%20liked/Subsets.py)
## **Example**

```python
Example : nums= [1,2,3]
# >>> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

```mathematica
backtrack(0)
├── Append [] to res
│
├── For i=0 (Include 1)
│   ├── subset = [1]
│   ├── backtrack(1)
│   │   ├── Append [1] to res
│   │   │
│   │   ├── For i=1 (Include 2)
│   │   │   ├── subset = [1,2]
│   │   │   ├── backtrack(2)
│   │   │   │   ├── Append [1,2] to res
│   │   │   │   │
│   │   │   │   ├── For i=2 (Include 3)
│   │   │   │   │   ├── subset = [1,2,3]
│   │   │   │   │   ├── backtrack(3)
│   │   │   │   │   │   ├── Append [1,2,3] to res
│   │   │   │   │   ├── Backtrack: Remove 3 → subset = [1,2]
│   │   │   │   ├── Returns
│   │   │   ├── Backtrack: Remove 2 → subset = [1]
│   │   │
│   │   ├── For i=2 (Include 3)
│   │   │   ├── subset = [1,3]
│   │   │   ├── backtrack(3)
│   │   │   │   ├── Append [1,3] to res
│   │   │   ├── Backtrack: Remove 3 → subset = [1]
│   │   ├── Returns
│   ├── Backtrack: Remove 1 → subset = []
│
├── For i=1 (Include 2)
│   ├── subset = [2]
│   ├── backtrack(2)
│   │   ├── Append [2] to res
│   │   │
│   │   ├── For i=2 (Include 3)
│   │   │   ├── subset = [2,3]
│   │   │   ├── backtrack(3)
│   │   │   │   ├── Append [2,3] to res
│   │   │   ├── Backtrack: Remove 3 → subset = [2]
│   │   ├── Returns
│   ├── Backtrack: Remove 2 → subset = []
│
├── For i=2 (Include 3)
│   ├── subset = [3]
│   ├── backtrack(3)
│   │   ├── Append [3] to res
│   ├── Backtrack: Remove 3 → subset = []
│
└── Return
```