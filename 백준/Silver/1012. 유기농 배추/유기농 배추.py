
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque([(x,y)])
    mat[x][y] = 0 

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0<= ny < M and mat[nx][ny] == 1:
                queue.append((nx,ny))
                mat[nx][ny] = 0

for _ in range(T):
    M,N,K = map(int,input().split())
    mat = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        p, q = map(int,input().split())
        mat[q][p] = 1 

    for a in range(N):
        for b in range(M):
            if mat[a][b] == 1:
                bfs(a,b)
                cnt += 1
                
            
    print(cnt)