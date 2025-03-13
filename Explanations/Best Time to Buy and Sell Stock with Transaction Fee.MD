## **Example**
---

```python
Example : prices = [1,3,2,8,4,9], fee = 2
# >>> 8
```
---
### **Step-by-Step Execution**
| Day | Price | `balance` (holding stock) | `profit` (not holding stock) |
|----|------|----------------------|------------------------|
| 0  |  1   | **-1** (buy)         |  0                      |
| 1  |  3   | **-1** (hold)        |  max(0, -1 + 3 - 2) = 0 |
| 2  |  2   | **-1** (hold)        |  0                      |
| 3  |  8   | **-1** (hold)        |  max(0, -1 + 8 - 2) = **5** (sell) |
| 4  |  4   | max(-1, 5 - 4) = **1** (buy) | **5** (hold cash) |
| 5  |  9   | **1** (hold)         | max(5, 1 + 9 - 2) = **8** (sell) |
