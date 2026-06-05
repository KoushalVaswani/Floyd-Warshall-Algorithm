def AllPaths(cost,n):
    A = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = cost[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j] , A[i][k]+A[k][j])
    return A
inf = 99999
n = 5
cost = [[0,4,inf,5,inf],
        [inf,0,1,inf,6],
        [2,inf,0,3,inf],
        [inf,inf,1,0,2],
        [1,inf,inf,4,0]]
shortest_path = AllPaths(cost , n)
print("The shortest path is : ")
for row in shortest_path:
    print(row)