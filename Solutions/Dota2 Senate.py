##############################################################################
# Wrong solution
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_q = deque(senate)
        if all(x == senate_q[0] for x in senate_q) or len(senate_q)==1:
            return "Radiant" if senate_q.pop() == "R" else "Dire"
        else:
            if senate_q.popleft() == "R" and "D" in senate_q:
                senate_q.remove("D")
            elif senate_q.popleft() == "D" and "R" in senate_q:
                senate_q.remove("R")
            return self.predictPartyVictory((senate_q))
##############################################################################
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)  
        radiant_bans = 0  
        dire_bans = 0 
        while queue:
            senator = queue.popleft()
            
            if senator == 'R':
                if radiant_bans > 0:                   
                    radiant_bans -= 1
                else:
                    dire_bans += 1
                    queue.append('R')

            elif senator == 'D':
                if dire_bans > 0:
                    dire_bans -= 1
                else:
                    radiant_bans += 1
                    queue.append('D')

            if all(s == 'R' for s in queue):
                return "Radiant"
            if all(s == 'D' for s in queue):
                return "Dire"
##############################################################################
s = Solution()
print(s.predictPartyVictory("RRDDDRDRD"))
# print(s.predictPartyVictory("DDD"))
# print(s.predictPartyVictory("RD"))
