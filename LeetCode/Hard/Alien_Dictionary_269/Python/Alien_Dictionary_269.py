from collections import defaultdict
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for word in words for c in word}
        in_degrees = {c: 0 for c in adj_list.keys()}

        def compWords(w1, w2):
            l1, l2 = len(w1), len(w2)
            if l1 > l2 and w1[:l2] == w2:
                return False
            for i in range(min(l1, l2)):
                if w1[i] != w2[i]:
                    adj_list[w1[i]].add(w2[i])
                    in_degrees[w2[i]] += 1
                    return True
            return True

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if not compWords(w1, w2):
                return ""
        print(adj_list)
        print(in_degrees)

        visited, visiting = {}, {}
        nodes_ord = []

        def dfs(node):
            if node in visiting and visiting[node]:
                return False
            if node not in visited:
                visited[node], visiting[node] = True, True
                for inode in adj_list[node]:
                    res = dfs(inode)
                    if not res:
                        return False
                visiting[node] = False
                nodes_ord.append(node)
            return True

        root = None
        for node in adj_list.keys():
            root = node
            res = dfs(root)
            if not res:
                return ""

        nodes_ord = list(reversed(nodes_ord))
        # print(root, res, nodes_ord)
        return "".join(nodes_ord)


