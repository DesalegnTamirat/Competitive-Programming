# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for one, two in dislikes:
            graph[one].append(two)
            graph[two].append(one)

        colors = defaultdict(int)
        def dfs(node):
            for neighbour in graph[node]:
                if colors[neighbour] == colors[node]:
                    return False
                if colors[neighbour] == 0:
                    colors[neighbour] = -colors[node]
                    if not dfs(neighbour):
                        return False
            
            return True

        for node in range(1, n + 1):
            if colors[node] == 0:
                colors[node] = 1
                if not dfs(node):
                    return False
        
        return True
            