
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneNodes = {}
        def dfs(node):
            if not node: return None
            if node in cloneNodes:
                return cloneNodes[node]
            copy = Node(node.val)
            cloneNodes[node] = copy
            copy.neighbors = [dfs(n) for n in node.neighbors]
            return copy
            
        return dfs(node)
        
