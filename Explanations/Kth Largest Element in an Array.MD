## Example : 
```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

---

### Initial State
- `min_heap = []`

---
#### 1. **First element (3)**:
   - `heapq.heappush(min_heap, 3)` adds 3 to the heap
   - Heap becomes: `[3]`
   - Heap size is 1, which is not > k, so don't pop
---
#### 2. **Second element (2)**:
   - `heapq.heappush(min_heap, 2)` adds 2 to the heap
   - During the push, heapq compares 2 with its parent (3):
     - Since 2 < 3, it swaps them to maintain the min-heap property
   - Heap becomes: `[2, 3]`
   - Heap size is 2, which is not > k, so don't pop

#### 3. **Third element (1)**:
   - `heapq.heappush(min_heap, 1)` adds 1 to the heap
   - During the push, heapq places 1 at the end (`[2, 3, 1]`) then "bubbles it up":
     - 1 is compared with its parent 2, and since 1 < 2, they swap
   - Heap becomes: `[1, 3, 2]`
   - Heap size is 3, which is > k (2), so call `heapq.heappop(min_heap)`
   - The pop removes the smallest element (1) and restructures the heap:
     - The last element (2) is moved to the root position
     - Then it "sifts down" by comparing with its children
   - Heap becomes: `[2, 3]`

#### 4. **Fourth element (5)**:
   - `heapq.heappush(min_heap, 5)` adds 5 to the heap
   - Heap becomes: `[2, 3, 5]`
   - Heap size is 3, which is > k (2), so we call `heapq.heappop(min_heap)`
   - The pop removes 2 and restructures the heap
   - Heap becomes: `[3, 5]`

#### 5. **Fifth element (6)**:
   - `heapq.heappush(min_heap, 6)` adds 6 to the heap
   - Heap becomes: `[3, 5, 6]`
   - Heap size is 3, which is > k (2), so we call `heapq.heappop(min_heap)`
   - The pop removes 3 and restructures the heap
   - Heap becomes: `[5, 6]`

#### 6. **Sixth element (4)**:
   - `heapq.heappush(min_heap, 4)` adds 4 to the heap
   - The push places 4 at the end, then bubbles it up if needed
   - Heap becomes: `[4, 6, 5]` 
   - Heap size is 3, which is > k (2), so we call `heapq.heappop(min_heap)`
   - The pop removes 4 and restructures the heap
   - Heap becomes: `[5, 6]`

### Final Result

- After processing all elements, heap contains `[5, 6]`
- The smallest element (at index 0) is 5, which is indeed the 2nd largest element in the original array (the largest being 6)


---
---

* In `6.` ,
```
    5         becomes        4
   /                        /  \
  6                        6    5
```

The key insight is that the heap is represented as an array, but the relationships between elements follow a binary tree structure. When new elements are added:

1. They first go to the end of the array
2. Then they "bubble up" by comparing with their parent and swapping if they're smaller
3. This continues until they reach their correct position
---
> ### Conclusion 
> ### **heaps - Arrays with a tree-like relationship between elements**