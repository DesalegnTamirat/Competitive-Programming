# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [0] * n
        for p1, p2 in trust:
            degrees[p1 - 1] -= 1
            degrees[p2 - 1] += 1
        
        for p in range(n):
            if degrees[p] == n - 1:
                return p + 1
        
        return -1

