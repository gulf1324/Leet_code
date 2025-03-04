## Solution2 recursion tree (Wrong)
### Example
```combinationSum3(k = 2, n = 6)```
```python
backtrack(0, [], 0)
├── index=0, combination=[], curr_sum=0, nums[0:]=[1, 2, 3, 4, 5, 6, 7, 8, 9]
│   ├── num=1
│   │   ├── Append 1: combination=[1]
│   │   └── backtrack(1, [1], 1)
│   │       ├── index=1, combination=[1], curr_sum=1, nums[1:]=[2, 3, 4, 5, 6, 7, 8, 9]
│   │       │   ├── num=2
│   │       │   │   ├── Append 2: combination=[1, 2]
│   │       │   │   └── backtrack(2, [1, 2], 3)
│   │       │   │       ├── len=2, curr_sum=3 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 2: combination=[1]
│   │       │   ├── num=3
│   │       │   │   ├── Append 3: combination=[1, 3]
│   │       │   │   └── backtrack(2, [1, 3], 4)
│   │       │   │       ├── len=2, curr_sum=4 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 3: combination=[1]
│   │       │   ├── num=4
│   │       │   │   ├── Append 4: combination=[1, 4]
│   │       │   │   └── backtrack(2, [1, 4], 5)
│   │       │   │       ├── len=2, curr_sum=5 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 4: combination=[1]
│   │       │   ├── num=5
│   │       │   │   ├── Append 5: combination=[1, 5]
│   │       │   │   └── backtrack(2, [1, 5], 6)
│   │       │   │       ├── len=2, curr_sum=6 == 6, match
│   │       │   │       ├── Add [1, 5] to res
│   │       │   │       └── Return
│   │       │   │   ├── Pop 5: combination=[1]
│   │       │   ├── num=6
│   │       │   │   ├── Append 6: combination=[1, 6]
│   │       │   │   └── backtrack(2, [1, 6], 7)
│   │       │   │       ├── curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 6: combination=[1]
│   │       │   └── [nums 7, 8, 9 pruned similarly]
│   │       └── Pop 1: combination=[]
│   ├── num=2
│   │   ├── Append 2: combination=[2]
│   │   └── backtrack(1, [2], 2)
│   │       ├── index=1, combination=[2], curr_sum=2, nums[1:]=[2, 3, 4, 5, 6, 7, 8, 9]
│   │       │   ├── num=2
│   │       │   │   ├── Append 2: combination=[2, 2]
│   │       │   │   └── backtrack(2, [2, 2], 4)
│   │       │   │       ├── len=2, curr_sum=4 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 2: combination=[2]
│   │       │   ├── num=3
│   │       │   │   ├── Append 3: combination=[2, 3]
│   │       │   │   └── backtrack(2, [2, 3], 5)
│   │       │   │       ├── len=2, curr_sum=5 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 3: combination=[2]
│   │       │   ├── num=4
│   │       │   │   ├── Append 4: combination=[2, 4]
│   │       │   │   └── backtrack(2, [2, 4], 6)
│   │       │   │       ├── len=2, curr_sum=6 == 6, match
│   │       │   │       ├── Add [2, 4] to res
│   │       │   │       └── Return
│   │       │   │   ├── Pop 4: combination=[2]
│   │       │   ├── num=5
│   │       │   │   ├── Append 5: combination=[2, 5]
│   │       │   │   └── backtrack(2, [2, 5], 7)
│   │       │   │       ├── curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 5: combination=[2]
│   │       │   └── [nums 6, 7, 8, 9 pruned]
│   │       └── Pop 2: combination=[]
│   ├── num=3
│   │   ├── Append 3: combination=[3]
│   │   └── backtrack(1, [3], 3)
│   │       ├── index=1, combination=[3], curr_sum=3, nums[1:]=[2, 3, 4, 5, 6, 7, 8, 9]
│   │       │   ├── num=2
│   │       │   │   ├── Append 2: combination=[3, 2]
│   │       │   │   └── backtrack(2, [3, 2], 5)
│   │       │   │       ├── len=2, curr_sum=5 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 2: combination=[3]
│   │       │   ├── num=3
│   │       │   │   ├── Append 3: combination=[3, 3] ###### duplicate occurs ######
│   │       │   │   └── backtrack(2, [3, 3], 6)
│   │       │   │       ├── len=2, curr_sum=6 == 6, match
│   │       │   │       ├── Add [3, 3] to res
│   │       │   │       └── Return
│   │       │   │   ├── Pop 3: combination=[3]
│   │       │   ├── num=4
│   │       │   │   ├── Append 4: combination=[3, 4]
│   │       │   │   └── backtrack(2, [3, 4], 7)
│   │       │   │       ├── curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 4: combination=[3]
│   │       │   └── [nums 5, 6, 7, 8, 9 pruned]
│   │       └── Pop 3: combination=[]
│   ├── num=4
│   │   ├── Append 4: combination=[4]
│   │   └── backtrack(1, [4], 4)
│   │       ├── index=1, combination=[4], curr_sum=4, nums[1:]=[2, 3, 4, 5, 6, 7, 8, 9]
│   │       │   ├── num=2
│   │       │   │   ├── Append 2: combination=[4, 2] ##### not in order as should be intended #####
│   │       │   │   └── backtrack(2, [4, 2], 6)
│   │       │   │       ├── len=2, curr_sum=6 == 6, match
│   │       │   │       ├── Add [4, 2] to res
│   │       │   │       └── Return
│   │       │   │   ├── Pop 2: combination=[4]
│   │       │   ├── num=3
│   │       │   │   ├── Append 3: combination=[4, 3]
│   │       │   │   └── backtrack(2, [4, 3], 7)
│   │       │   │       ├── curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 3: combination=[4]
│   │       │   └── [nums 4, 5, 6, 7, 8, 9 pruned]
│   │       └── Pop 4: combination=[]
│   └── [num=5, 6, 7, 8, 9 lead to curr_sum >= 6 early, pruned]
└── Return res = [[1, 5], [2, 4], [3, 3], [4, 2]]
```

---
## Solution4 recursion tree (Best)
### Example
```combinationSum3(k = 2, n = 6)```
```python
backtrack(1, [], 0)
├── index=1, combination=[], curr_sum=0, range(1, 10)=[1, 2, 3, 4, 5, 6, 7, 8, 9]
│   ├── i=1
│   │   ├── Append 1: combination=[1]
│   │   └── backtrack(2, [1], 1)
│   │       ├── index=2, combination=[1], curr_sum=1, range(2, 10)=[2, 3, 4, 5, 6, 7, 8, 9]
│   │       │   ├── i=2
│   │       │   │   ├── Append 2: combination=[1, 2]
│   │       │   │   └── backtrack(3, [1, 2], 3)
│   │       │   │       ├── len=2, curr_sum=3 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 2: combination=[1]
│   │       │   ├── i=3
│   │       │   │   ├── Append 3: combination=[1, 3]
│   │       │   │   └── backtrack(4, [1, 3], 4)
│   │       │   │       ├── len=2, curr_sum=4 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 3: combination=[1]
│   │       │   ├── i=4
│   │       │   │   ├── Append 4: combination=[1, 4]
│   │       │   │   └── backtrack(5, [1, 4], 5)
│   │       │   │       ├── len=2, curr_sum=5 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 4: combination=[1]
│   │       │   ├── i=5
│   │       │   │   ├── Append 5: combination=[1, 5]
│   │       │   │   └── backtrack(6, [1, 5], 6)
│   │       │   │       ├── len=2, curr_sum=6 == 6, match
│   │       │   │       ├── Add [1, 5] to res
│   │       │   │       └── Return
│   │       │   │   ├── Pop 5: combination=[1]
│   │       │   ├── i=6
│   │       │   │   ├── Append 6: combination=[1, 6]
│   │       │   │   └── backtrack(7, [1, 6], 7)
│   │       │   │       ├── len=2, curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 6: combination=[1]
│   │       │   └── [i=7, 8, 9 pruned by sum]
│   │       └── Pop 1: combination=[]
│   ├── i=2
│   │   ├── Append 2: combination=[2]
│   │   └── backtrack(3, [2], 2)
│   │       ├── index=3, combination=[2], curr_sum=2, range(3, 10)=[3, 4, 5, 6, 7, 8, 9]
│   │       │   ├── i=3
│   │       │   │   ├── Append 3: combination=[2, 3]
│   │       │   │   └── backtrack(4, [2, 3], 5)
│   │       │   │       ├── len=2, curr_sum=5 < 6, no match
│   │       │   │       └── Return
│   │       │   │   ├── Pop 3: combination=[2]
│   │       │   ├── i=4
│   │       │   │   ├── Append 4: combination=[2, 4]
│   │       │   │   └── backtrack(5, [2, 4], 6)
│   │       │   │       ├── len=2, curr_sum=6 == 6, match
│   │       │   │       ├── Add [2, 4] to res
│   │       │   │       └── Return
│   │       │   │   ├── Pop 4: combination=[2]
│   │       │   ├── i=5
│   │       │   │   ├── Append 5: combination=[2, 5]
│   │       │   │   └── backtrack(6, [2, 5], 7)
│   │       │   │       ├── len=2, curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 5: combination=[2]
│   │       │   └── [i=6, 7, 8, 9 pruned by sum]
│   │       └── Pop 2: combination=[]
│   ├── i=3
│   │   ├── Append 3: combination=[3]
│   │   └── backtrack(4, [3], 3)
│   │       ├── index=4, combination=[3], curr_sum=3, range(4, 10)=[4, 5, 6, 7, 8, 9]
│   │       │   ├── i=4
│   │       │   │   ├── Append 4: combination=[3, 4]
│   │       │   │   └── backtrack(5, [3, 4], 7)
│   │       │   │       ├── len=2, curr_sum=7 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 4: combination=[3]
│   │       │   ├── i=5
│   │       │   │   ├── Append 5: combination=[3, 5]
│   │       │   │   └── backtrack(6, [3, 5], 8)
│   │       │   │       ├── len=2, curr_sum=8 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 5: combination=[3]
│   │       │   └── [i=6, 7, 8, 9 pruned by sum]
│   │       └── Pop 3: combination=[]
│   ├── i=4
│   │   ├── Append 4: combination=[4]
│   │   └── backtrack(5, [4], 4)
│   │       ├── index=5, combination=[4], curr_sum=4, range(5, 10)=[5, 6, 7, 8, 9]
│   │       │   ├── i=5
│   │       │   │   ├── Append 5: combination=[4, 5]
│   │       │   │   └── backtrack(6, [4, 5], 9)
│   │       │   │       ├── len=2, curr_sum=9 >= 6, prune
│   │       │   │       └── Return
│   │       │   │   ├── Pop 5: combination=[4]
│   │       │   └── [i=6, 7, 8, 9 pruned by sum]
│   │       └── Pop 4: combination=[]
│   └── [i=5, 6, 7, 8, 9 lead to curr_sum >= 6 early, pruned]
└── Return res = [[1, 5], [2, 4]]
```