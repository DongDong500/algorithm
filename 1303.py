"""
https://www.acmicpc.net/problem/1303

BFS
"""

def BFS(N, M, MAP, visited, strpnt):
    cnt = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    Q = deque()
    Q.append(strpnt)

    while Q:
        x, y = Q.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and MAP[x][y] == MAP[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))
                cnt += 1
    return cnt

if __name__ == "__main__":

    from collections import deque

    N, M = map(int, input().split())

    MAP = [list(input()) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    blue, white = 0, 0

    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0:
                cnt = BFS(N, M, MAP, visited, (i, j))
                if MAP[i][j] == "W": white += cnt**2
                else: blue += cnt**2

print(white, blue)