from typing import List
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj = {}
        if len(edges) == 0:
            return len(vals)
        for edge in edges:
            # print("edge = ", edge)
            if edge[0] in adj:
                adj[edge[0]].add(edge[1])
            else:
                adj[edge[0]] = set([edge[1]])

            if edge[1] in adj:
                adj[edge[1]].add(edge[0])
            else:
                adj[edge[1]] = set([edge[0]])
        # print("adj = ", adj)
        visited = set()

        def dfs(i, tgt):
            visited.add(i)
            tgps = 0
            for j in adj[i]:
                jval = vals[j]
                if j not in visited and jval <= tgt:
                    tgps += dfs(j, tgt)
            ival = vals[i]
            if ival == tgt:
                tgps += 1
            return tgps

        tgps = 0
        multipaths = 0
        for i, v in enumerate(vals):
            visited = set()
            res = dfs(i, v)
            if res > 1:
                multipaths += res - 1
            # print("res, i, v = ", res, i, v)
            tgps += res

        return tgps - multipaths // 2
