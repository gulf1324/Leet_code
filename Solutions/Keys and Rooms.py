#####################################################################################
# DFS
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        room_opened = set()
        room_keys = [0]
        while room_keys:
            ############################
            room_key = room_keys.pop() #
            ############################
            if room_key in room_opened:
                continue
            room_opened.add(room_key)
            for key in rooms[room_key]:
                if key not in room_opened:
                    room_keys.append(key)
        return len(room_opened) == len(rooms)
#####################################################################################    
# BFS
from collections import deque
class Solution2:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        room_opened = set()
        room_keys = deque([0])
        while room_keys:
            ################################
            room_key = room_keys.popleft() #
            ################################
            if room_key in room_opened:
                continue
            room_opened.add(room_key)
            for key in rooms[room_key]:
                if key not in room_opened:
                    room_keys.append(key)
        return len(room_opened) == len(rooms)
#####################################################################################    
s = Solution()
print(s.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))
# False
print(s.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
# True