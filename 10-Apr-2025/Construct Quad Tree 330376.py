# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def do(row1, col1, row2, col2):
            if row1 > row2:
                return None
            
            n = row2 - row1 + 1
            values = set()
            same = True
            for row in range(row1, row2 + 1):
                for col in range(col1, col2 + 1):
                    values.add(grid[row][col])
                    if len(values) == 2:
                        same = False
                        break
                if not same:
                    break
            
            if same:
                return Node(grid[row1][col1], True, None, None, None, None)
            
            newNode = Node(0)
            
            newNode.topLeft = do(row1, col1, row1 + n // 2 - 1, col1 + n // 2 - 1)
            newNode.topRight = do(row1, col1 + n // 2, row1 + n // 2 - 1, col2)
            newNode.bottomLeft = do(row1 + n // 2, col1, row2, col1 + n // 2 - 1)
            newNode.bottomRight = do(row1 + n // 2, col1 + n // 2, row2, col2)

            return newNode

        return do(0, 0, len(grid) - 1, len(grid) - 1)