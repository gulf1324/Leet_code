Code: [Validate Binary Search Tree.py](../../Solutions/Top%20100%20liked/Validate%20Binary%20Search%20Tree.py)
# Example : 
>```python
> root = [10, 5, 15, 3, 7, 9, 20]
> # >>> False 
>```
```
          10
         /  \
        5    15
       / \   / \
      3   7 9  20
```
---

```python 
# DFS recursion
validate(10, -∞, ∞) → ✅
├── validate(5, -∞, 10) → ✅
│   ├── validate(3, -∞, 5) → ✅
│   │   ├── validate(None, -∞, 3) → ✅
│   │   └── validate(None, 3, 5) → ✅
│   └── validate(7, 5, 10) → ✅
│       ├── validate(None, 5, 7) → ✅
│       └── validate(None, 7, 10) → ✅
└── validate(15, 10, ∞) → ✅
    ├── validate(9, 10, 15) → ❌
  # │   ├── validate(None, 10, 9) → ✅
  # │   └── validate(None, 9, 15) → ✅
  # └── validate(20, 15, ∞) → ✅
  #     ├── validate(None, 15, 20) → ✅
  #     └── validate(None, 20, ∞) → ✅
```