## Example :
```python
equations = [["a","b"], ["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"], ["b","a"], ["a","e"]]
```
---
### 1. Building the graph (`relatives`):
```python
relatives = defaultdict(list)

# First equation: ["a","b"] with value 2.0
relatives["a"].append((2.0, "b"))    # a -> b = 2.0
relatives["b"].append((1/2.0, "a"))  # b -> a = 0.5

# Second equation: ["b","c"] with value 3.0
relatives["b"].append((3.0, "c"))    # b -> c = 3.0
relatives["c"].append((1/3.0, "b"))  # c -> b = 0.333...

# {
#   'a': [(2.0, 'b')],
#   'b': [(0.5, 'a'), (3.0, 'c')],
#   'c': [(0.333..., 'b')]
# }
```
---
### 2. DFS:

Query 1: ["a","c"]
```python
dfs("a", "c", set())
├── start="a", end="c", visited=set()
│   ├── "a" in relatives? Yes
│   ├── "a" == "c"? No
│   ├── Add "a" to visited: {'a'}
│   │
│   ├── Check neighbor (2.0, "b"):
│   │   └── dfs("b", "c", {'a'})
│   │       ├── "b" in relatives? Yes
│   │       ├── "b" == "c"? No
│   │       ├── Add "b" to visited: {'a', 'b'}
│   │       │
│   │       ├── Check neighbor (0.5, "a"):
│   │       │   └── Skip ("a" in visited)
│   │       │
│   │       ├── Check neighbor (3.0, "c"):
│   │       │   └── dfs("c", "c", {'a', 'b'})
│   │       │       ├── "c" == "c"? Yes
│   │       │       └── Return 1.0
│   │       └── Return 3.0 * 1.0 = 3.0
│   └── Return 2.0 * 3.0 = 6.0
```

Query 2: ["b","a"]
```python
dfs("b", "a", set())
├── start="b", end="a", visited=set()
│   ├── "b" in relatives? Yes
│   ├── "b" == "a"? No
│   ├── Add "b" to visited: {'b'}
│   │
│   ├── Check neighbor (0.5, "a"):
│   │   └── dfs("a", "a", {'b'})
│   │       ├── "a" == "a"? Yes
│   │       └── Return 1.0
│   └── Return 0.5 * 1.0 = 0.5
```

Query 3: ["a","e"]
```python
# "e" not in relatives, immediately return -1.0
```

Final result: `[6.0, 0.5, -1.0]`

1. Build a graph where edges represent division relationships
   - If a/b = 2, then b/a = 1/2
2. ex) a/c :
   - Start at 'a'
   - Follow path to 'c'
   - Multiply all values along the path
3. If no path exists or variable doesn't exist: return -1


### 2-1 BFS:
Iterative using ```deque()```