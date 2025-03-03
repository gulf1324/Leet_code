## Example :
```python
digits = "23"
# >>> ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```
---

```python
# recursive
backtrack(0, [])
├── index=0, digits="23", path=[]
│   ├── index == len(digits)? No (0 != 2)
│   ├── For digit "2", letters are "abc"
│   │
│   ├── Iteration: char = 'a'
│   │   ├── Add 'a' to path: ['a']
│   │   └── backtrack(1, ['a'])
│   │       ├── index == len(digits)? No (1 != 2)
│   │       ├── For digit "3", letters are "def"
│   │       │
│   │       ├── Iteration: char = 'd'
│   │       │   ├── Add 'd' to path: ['a', 'd']
│   │       │   └── backtrack(2, ['a', 'd'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "ad" to result: ["ad"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'd' from path: ['a']
│   │       │
│   │       ├── Iteration: char = 'e'
│   │       │   ├── Add 'e' to path: ['a', 'e']
│   │       │   └── backtrack(2, ['a', 'e'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "ae" to result: ["ad", "ae"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'e' from path: ['a']
│   │       │
│   │       ├── Iteration: char = 'f'
│   │       │   ├── Add 'f' to path: ['a', 'f']
│   │       │   └── backtrack(2, ['a', 'f'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "af" to result: ["ad", "ae", "af"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'f' from path: ['a']
│   │       └── Return to previous call
│   │   ├── Remove 'a' from path: []
│   │
│   ├── Iteration: char = 'b'
│   │   ├── Add 'b' to path: ['b']
│   │   └── backtrack(1, ['b'])
│   │       ├── index == len(digits)? No (1 != 2)
│   │       ├── For digit "3", letters are "def"
│   │       │
│   │       ├── Iteration: char = 'd'
│   │       │   ├── Add 'd' to path: ['b', 'd']
│   │       │   └── backtrack(2, ['b', 'd'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "bd" to result: ["ad", "ae", "af", "bd"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'd' from path: ['b']
│   │       │
│   │       ├── Iteration: char = 'e'
│   │       │   ├── Add 'e' to path: ['b', 'e']
│   │       │   └── backtrack(2, ['b', 'e'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "be" to result: ["ad", "ae", "af", "bd", "be"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'e' from path: ['b']
│   │       │
│   │       ├── Iteration: char = 'f'
│   │       │   ├── Add 'f' to path: ['b', 'f']
│   │       │   └── backtrack(2, ['b', 'f'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "bf" to result: ["ad", "ae", "af", "bd", "be", "bf"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'f' from path: ['b']
│   │       └── Return to previous call
│   │   ├── Remove 'b' from path: []
│   │
│   ├── Iteration: char = 'c'
│   │   ├── Add 'c' to path: ['c']
│   │   └── backtrack(1, ['c'])
│   │       ├── index == len(digits)? No (1 != 2)
│   │       ├── For digit "3", letters are "def"
│   │       │
│   │       ├── Iteration: char = 'd'
│   │       │   ├── Add 'd' to path: ['c', 'd']
│   │       │   └── backtrack(2, ['c', 'd'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "cd" to result: ["ad", "ae", "af", "bd", "be", "bf", "cd"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'd' from path: ['c']
│   │       │
│   │       ├── Iteration: char = 'e'
│   │       │   ├── Add 'e' to path: ['c', 'e']
│   │       │   └── backtrack(2, ['c', 'e'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "ce" to result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'e' from path: ['c']
│   │       │
│   │       ├── Iteration: char = 'f'
│   │       │   ├── Add 'f' to path: ['c', 'f']
│   │       │   └── backtrack(2, ['c', 'f'])
│   │       │       ├── index == len(digits)? Yes (2 == 2)
│   │       │       ├── Add "cf" to result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
│   │       │       └── Return to previous call
│   │       │   ├── Remove 'f' from path: ['c']
│   │       └── Return to previous call
│   │   ├── Remove 'c' from path: []
│   │
│   └── Final result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```
---
```python
# iterative (BFS)
├── Initialize:
│   ├── result = []
│   └── queue = deque([(0, [])])
│
├── Iteration 1:
│   ├── Popleft (0, []) from queue
│   ├── index=0, digits="23", path=[]
│   ├── index == len(digits)? No (0 != 2)
│   ├── digit = "2", letters = "abc"
│   ├── Add to queue:
│   │   ├── (1, ['a'])
│   │   ├── (1, ['b'])
│   │   └── (1, ['c'])
│   └── queue = deque([(1, ['a']), (1, ['b']), (1, ['c'])])
│
├── Iteration 2:
│   ├── Popleft (1, ['a']) from queue
│   ├── index=1, digits="23", path=['a']
│   ├── index == len(digits)? No (1 != 2)
│   ├── digit = "3", letters = "def"
│   ├── Add to queue:
│   │   ├── (2, ['a', 'd'])
│   │   ├── (2, ['a', 'e'])
│   │   └── (2, ['a', 'f'])
│   └── queue = deque([(1, ['b']), (1, ['c']), (2, ['a', 'd']), (2, ['a', 'e']), (2, ['a', 'f'])])
│
├── Iteration 3:
│   ├── Popleft (1, ['b']) from queue
│   ├── index=1, digits="23", path=['b']
│   ├── index == len(digits)? No (1 != 2)
│   ├── digit = "3", letters = "def"
│   ├── Add to queue:
│   │   ├── (2, ['b', 'd'])
│   │   ├── (2, ['b', 'e'])
│   │   └── (2, ['b', 'f'])
│   └── queue = deque([(1, ['c']), (2, ['a', 'd']), (2, ['a', 'e']), (2, ['a', 'f']), 
│                      (2, ['b', 'd']), (2, ['b', 'e']), (2, ['b', 'f'])])
│
├── Iteration 4:
│   ├── Popleft (1, ['c']) from queue
│   ├── index=1, digits="23", path=['c']
│   ├── index == len(digits)? No (1 != 2)
│   ├── digit = "3", letters = "def"
│   ├── Add to queue:
│   │   ├── (2, ['c', 'd'])
│   │   ├── (2, ['c', 'e'])
│   │   └── (2, ['c', 'f'])
│   └── queue = deque([(2, ['a', 'd']), (2, ['a', 'e']), (2, ['a', 'f']), 
│                     (2, ['b', 'd']), (2, ['b', 'e']), (2, ['b', 'f']),
│                     (2, ['c', 'd']), (2, ['c', 'e']), (2, ['c', 'f'])])
│
├── Iteration 5:
│   ├── Popleft (2, ['a', 'd']) from queue
│   ├── index=2, digits="23", path=['a', 'd']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "ad" to result: ["ad"]
│   └── queue has 8 remaining items
│
├── Iteration 6:
│   ├── Popleft (2, ['a', 'e']) from queue
│   ├── index=2, digits="23", path=['a', 'e']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "ae" to result: ["ad", "ae"]
│   └── queue has 7 remaining items
│
├── Iteration 7:
│   ├── Popleft (2, ['a', 'f']) from queue
│   ├── index=2, digits="23", path=['a', 'f']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "af" to result: ["ad", "ae", "af"]
│   └── queue has 6 remaining items
│
├── Iteration 8:
│   ├── Popleft (2, ['b', 'd']) from queue
│   ├── index=2, digits="23", path=['b', 'd']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "bd" to result: ["ad", "ae", "af", "bd"]
│   └── queue has 5 remaining items
│
├── Iteration 9:
│   ├── Popleft (2, ['b', 'e']) from queue
│   ├── index=2, digits="23", path=['b', 'e']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "be" to result: ["ad", "ae", "af", "bd", "be"]
│   └── queue has 4 remaining items
│
├── Iteration 10:
│   ├── Popleft (2, ['b', 'f']) from queue
│   ├── index=2, digits="23", path=['b', 'f']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "bf" to result: ["ad", "ae", "af", "bd", "be", "bf"]
│   └── queue has 3 remaining items
│
├── Iteration 11:
│   ├── Popleft (2, ['c', 'd']) from queue
│   ├── index=2, digits="23", path=['c', 'd']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "cd" to result: ["ad", "ae", "af", "bd", "be", "bf", "cd"]
│   └── queue has 2 remaining items
│
├── Iteration 12:
│   ├── Popleft (2, ['c', 'e']) from queue
│   ├── index=2, digits="23", path=['c', 'e']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "ce" to result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce"]
│   └── queue has 1 remaining item
│
├── Iteration 13:
│   ├── Popleft (2, ['c', 'f']) from queue
│   ├── index=2, digits="23", path=['c', 'f']
│   ├── index == len(digits)? Yes (2 == 2)
│   ├── Add "cf" to result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
│   └── queue is empty
│
└── Return result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```
---