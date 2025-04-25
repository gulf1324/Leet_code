Code: [Diameter of Binary Tree.py](../../Solutions/Top%20100%20liked/Diameter%20of%20Binary%20Tree.py)
# Example : 
>```python
> root = [1,2,3,4,5]
> # >>> 3 
>```
> ![Diameter of Binary Tree](./Diameter%20of%20Binary%20Tree.jpg)
---

```python 
dfs(1)
├── dfs(2)
│   ├── dfs(4)
│   │   ├── dfs(None) → 0
│   │   └── dfs(None) → 0
│   │   return 1 | self.max_diameter = 0
│   └── dfs(5)
│       ├── dfs(None) → 0
│       └── dfs(None) → 0
│       return 1 | self.max_diameter = 0
│   return 2 | self.max_diameter = 2
└── dfs(3)
    ├── dfs(None) → 0
    └── dfs(None) → 0
    return 1 | self.max_diameter = 2
return 3 | self.max_diameter = 3
```