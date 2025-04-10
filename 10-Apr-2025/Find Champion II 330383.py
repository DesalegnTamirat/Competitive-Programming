# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winner = defaultdict(int)
        for a, b in edges:
            winner[b] += 1
        
        answer = []
        for team in range(n):
            if winner[team] == 0:
                answer.append(team)
        
        return answer[0] if len(answer) == 1 else -1
