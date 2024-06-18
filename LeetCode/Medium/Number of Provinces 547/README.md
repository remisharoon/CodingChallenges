
## 'Number of Provinces' Algorithm Implementation

### Introduction
The 'Number of Provinces' problem is a classic example of an application of the Disjoint Set Union (DSU) or Union-Find algorithm. This Python script implements a solution to determine the number of provinces (or connected components) in an undirected graph, where the graph is represented as an adjacency matrix.

### Algorithm Explanation
The solution utilizes the Disjoint Set Union (DSU) structure to efficiently manage and merge sets of cities. Each province is a set of directly or indirectly connected cities. The main operations of the DSU are 'find' and 'union':
1. Find: This operation determines the representative or "parent" of the set containing the city. It employs path compression to flatten the structure of the tree, speeding up future operations.
2. Union: This operation merges two different sets into a single set. It involves finding the roots of the sets of both elements and making one root the parent of the other. This script implements the union by rank based on the index of the city (though the actual "rank" is not explicitly managed).

### Code Walkthrough
- Initialization:
  - `n`: The number of cities, derived from the length of the `isConnected` matrix.
  - `pcl`: Parent city list where each city initially points to itself.
- Iteration and Union:
  - Double loop through each city pair to check if they are connected.
  - If two cities are connected, attempt to union them, decreasing the count of provinces if successful.
- Return:
  - The number of distinct provinces, which is the final count of unique sets after all unions.
