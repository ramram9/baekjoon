import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
con = [[0]*(N+1) for _ in range(N+1)]

for _ in range(T):
    p,q = map(int,input().split())
    con[p][q] = con[q][p] = 1

visited = [False]*(N+1)
result = []
def dfs(matrix, start_node, visited):
    visited[start_node] = True
    for i in range(1,N+1):
        if matrix[start_node][i] == 1 and not visited[i]:
            result.append(i)
            dfs(matrix, i, visited) 

dfs(con, 1,visited)
print(len(result))