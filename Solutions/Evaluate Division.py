from collections import defaultdict, deque
#################################################################################################################################
# DFS, defaultdict(list)
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        relatives = defaultdict(list)
        res = []

        for equation, value in zip(equations, values):
            var_1, var_2 = equation[0], equation[1]
            relatives[var_1].append((value, var_2))
            relatives[var_2].append((1/value, var_1))
            # ex) defaultdict(<class 'list'>, 
            # {'a': [(2.0, 'b')], 
            #  'b': [(0.5, 'a'), (3.0, 'c')],
            #  'c': [(0.3333333333333333, 'b')]})
        
        def dfs(start: str, end: str, visited: set) -> float:
            if start not in relatives:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)

            for value, neighbor in relatives[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            return -1.0

        for start, end in queries:
            if end in relatives:
                result = dfs(start, end, set())
                res.append(result)
            else:
                res.append(-1.0)       
        return res
#################################################################################################################################
# BFS, defaultdict(dict)
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value 
        
        # ex) defaultdict(<class 'dict'>, 
        # {'a': {'b': 2.0},
        #  'b': {'a': 0.5, 'c': 3.0},
        #  'c': {'b': 0.3333333333333333}})
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0 
            
            queue = deque([(start, 1.0)])  # (node, current_product)
            visited = set()
            
            while queue:
                
                ## popleft() -> pop() == bfs -> dfs ##
                node, product = queue.popleft()      #
                ######################################
                
                if node == end:
                    return product  
                
                visited.add(node)
                
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            
            return -1.0 
        
        return [bfs(C, D) for C, D in queries]
#################################################################################################################################    
s = Solution()
print(s.calcEquation(equations = [["a","b"],["b","c"]], 
                     values = [2.0,3.0], 
                     queries = [["a","c"],["b","a"],["a","e"]]
                     ))
# >>> [6.0, 0.5, -1.0]