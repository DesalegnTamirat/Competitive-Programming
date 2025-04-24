# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid), len(grid[-1])
        ones = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    grid[row][col] = 0
                elif grid[row][col] == 1:
                    ones += 1
        
        in_bound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        answer = 0
        while queue:
            row, col, time = queue.popleft()
            answer = max(answer, time)
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if in_bound(new_row, new_col) and grid[new_row][new_col] == 1:
                    ones -= 1
                    queue.append((new_row, new_col, time + 1))
                    grid[new_row][new_col] = 0
                
        if not ones:
            return answer
        
        return -1