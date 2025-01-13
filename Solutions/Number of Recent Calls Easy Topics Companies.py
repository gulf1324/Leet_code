#########################################################
import queue
class RecentCounter:
    def __init__(self):
        self.ping_queue= queue.Queue()
    def ping(self, t: int) -> int:
        self.ping_queue.put(t)
        for elements in list(self.ping_queue.queue):
            if t-3000 > elements:
                self.ping_queue.get()
        return self.ping_queue.qsize()
#########################################################
class RecentCounter:
    def __init__(self):
        self.requests = []  
        self.start = 0      
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1  # Move the pointer to the right
        # The window size is the number of requests from `self.start` to the end of the list
        return len(self.requests) - self.start
#########################################################
# deque => task frequently edits both ends of a list 
from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)
#########################################################
obj = RecentCounter()
inputs = [1, 100, 3001, 3002]
res = []
for t in inputs:
    res.append(obj.ping(t))
print(res)