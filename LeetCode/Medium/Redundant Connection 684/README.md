
# Redundant Connection Solution

This repository contains my solution to the LeetCode problem "Redundant Connection" ([Problem 684](https://leetcode.com/problems/redundant-connection/description/)). The problem involves identifying an edge that can be removed from a graph to form a tree with `n` nodes.

## Problem Description

In this problem, you are given a graph that started as a tree with `n` nodes (labeled from 1 to n), with one additional edge added. This extra edge involves two different vertices chosen from 1 to n, and was not an edge that already existed. You need to return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If multiple answers exist, the answer that occurs last in the input should be returned.

## Solution

The solution uses the union-find data structure to detect cycles in the graph. Here's a brief overview of how the union-find operates in this solution:

- **Initialization**: A parent array is initialized where each node is its own parent.
- **Find Operation**: Determines the root parent of a node. Uses path compression for efficiency.
- **Union Operation**: Connects two nodes. If they are already connected (i.e., they have the same root parent), it detects a cycle.

### Python Code

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i+1 for i in range(len(edges))]

        def find(n):
            npar = n
            while npar != par[npar-1]:
                npar = par[npar-1]
            return npar
        
        def union(n1, n2):
            n1par = find(n1)
            n2par = find(n2)
            if n1par == n2par:
                return 0
            elif n1par < n2par:
                par[n2par-1] = n1par
            else:
                par[n1par-1] = n2par
            return 1

        for e in edges:
            n1, n2 = e[0], e[1]
            ret = union(n1, n2)
            if ret == 0:
                return e
```

## Example

Input: `edges = [[1,2],[1,3],[2,3]]`Output: `[2,3]`

Input: `edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]`Output: `[1,4]`

This solution is efficient and solves the problem as specified.
