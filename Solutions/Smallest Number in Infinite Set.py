import heapq
#################################################################################################################################################################
# Wrong
# does not prevent re-adding the same number
class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.added_back = []

    def popSmallest(self) -> int:
        # if some were added, return the smallest among them
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            return smallest
        # else return the current value (and as if it's popped)
        else:
            smallest = self.current
            self.current += 1 
            return smallest

    # only affects the result when num < self.current because:
    # popSmallest() only returns the smallest value
    def addBack(self, num: int) -> None:
        if num < self.current:
            heapq.heappush(self.added_back, num)
#################################################################################################################################################################
# Correct
# prevents duplicate
class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.added_back = set()

    def addBack(self, num: int):
        if num < self.current:
            self.added_back.add(num)

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = min(self.added_back)
            self.added_back.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest
#################################################################################################################################################################
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

obj = None
result = []

# Test 1
# query = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# input = [[], [2], [], [], [], [1], [], [], []]

# Test 2
query = ["SmallestInfiniteSet", "popSmallest", "addBack", "addBack", "popSmallest", "popSmallest"]
input = [[], [], [1], [1], [], []]

for q, i in zip(query, input):
    if q == "SmallestInfiniteSet":
        obj = SmallestInfiniteSet()
        result.append(None)  # Constructor doesn't return anything
    elif q == "addBack":
        obj.addBack(i[0])
        result.append(None)  # addBack doesn't return anything
    elif q == "popSmallest":
        result.append(obj.popSmallest())  # popSmallest returns an integer

print(result)
# Test 1
# >>> [None, None, 1, 2, 3, None, 1, 4, 5]

# Test 2
# >>> [None, 1, None, None, 1, 1] (x)
# >>> [None, 1, None, None, 1, 2] (o)