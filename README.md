# Graph-Algorithms-Python3
This repository contains a collection of graph algorithms implemented in Python 3.

### Contents

**Undirected Graph Algorithms:**
- Depth-First Search (DFS) - \(O(V + E)\)
- Breadth-First Search (BFS) - \(O(V + E)\)
- Connected Components - \(O(V + E)\)
- Bipartite Graph Validation - \(O(V + E)\)
- Cycle Detection - \(O(V + E)\)
- Eulerian Cycle/Path - \(O(EV + E^2)\)
- Hamiltonian Path (Backtracking) - Exponential Complexity

**Directed Graph (Digraph) Algorithms:**
- Depth-First Search (DFS) - \(O(V + E)\)
- Breadth-First Search (BFS) - \(O(V + E)\)
- Topological Sort (for DAGs) - \(O(V + E)\)
- Directed Cycle Detection - \(O(V + E)\)
- Strong Components (Kosaraju-Sharir Algorithm) - \(O(V + E)\)
- Shortest Ancestral Path (SAP) - \(O(V + E)\)

**Edge-Weighted Graph Minimum Spanning Tree (MST) Algorithms:**
- Kruskal's Algorithm - \(O(E log E)\)
- Prim's Algorithm (Lazy Implementation) - \(O(E log E)\)
- Prim's Algorithm (Eager Implementation) - \(O(E log V)\)

**Shortest Path in Edge-Weighted Digraph Algorithms:**
- Dijkstra's Algorithm - \(O(E \log V)\)
- Topological Sort (for shortest path in DAGs) - \(O(V + E)\)
- Bellman-Ford Algorithm - \(O(EV)\)
- Bellman-Ford Algorithm (Queue-Based) - Typically \(O(E + V)\), Worst Case \(O(EV)\)

**Flow Network Algorithms:**
- Maxflow/MinCut Problem (Ford-Fulkerson Algorithm)
