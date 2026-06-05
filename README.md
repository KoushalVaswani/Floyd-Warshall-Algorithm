# Floyd-Warshall Algorithm in Python

This project implements the Floyd-Warshall Algorithm to compute the shortest paths between all pairs of vertices in a weighted directed graph.

## 📌 Problem Statement

Given a weighted directed graph represented as a cost matrix, find the shortest distance between every pair of vertices.

## 📊 Input Cost Matrix

Here, `∞` represents that no direct edge exists between the corresponding vertices.

| From/To | 0 | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|---|
| 0 | 0 | 4 | ∞ | 5 | ∞ |
| 1 | ∞ | 0 | 1 | ∞ | 6 |
| 2 | 2 | ∞ | 0 | 3 | ∞ |
| 3 | ∞ | ∞ | 1 | 0 | 2 |
| 4 | 1 | ∞ | ∞ | 4 | 0 |

## 🔗 Graph Edges

- 0 → 1 (4)
- 0 → 3 (5)
- 1 → 2 (1)
- 1 → 4 (6)
- 2 → 0 (2)
- 2 → 3 (3)
- 3 → 2 (1)
- 3 → 4 (2)
- 4 → 0 (1)
- 4 → 3 (4)

## 🚀 Algorithm

The Floyd-Warshall Algorithm uses dynamic programming and updates the shortest distance matrix using:

```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

where `k` is considered as an intermediate vertex.

## 💻 Python Implementation

```python
def AllPaths(cost, n):
    A = [row[:] for row in cost]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    return A
```

## 📈 Expected Output

Shortest Path Matrix:

| From/To | 0 | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|---|
| 0 | 0 | 4 | 5 | 5 | 7 |
| 1 | 3 | 0 | 1 | 4 | 6 |
| 2 | 2 | 6 | 0 | 3 | 5 |
| 3 | 3 | 7 | 1 | 0 | 2 |
| 4 | 1 | 5 | 5 | 4 | 0 |

## ⏱️ Time Complexity

```
O(V³)
```

where `V` is the number of vertices.

## 💾 Space Complexity

```
O(V²)
```

## 🎯 Applications

- Network Routing
- Traffic Navigation Systems
- Airline Route Optimization
- Computer Network Analysis
- Social Network Analysis
- Path Finding Problems

## 🛠️ Technologies Used

- Python 3
- Dynamic Programming
- Graph Algorithms

## 📚 References

- Introduction to Algorithms (CLRS)
- Data Structures and Algorithms
- Graph Theory Fundamentals
